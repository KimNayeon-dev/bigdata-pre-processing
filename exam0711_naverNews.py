# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## <NAVER 웹 크롤링>
# ### NAVER 뉴스 분석 및 시각화(워드 클라우드)
# ---
# > 코앤엘파이(konlpy)<br>
# > 파이태그클라우드(pytagcloud)
# - <Step1. 웹 크롤링> - 웹 크롤링으로 데이터를 가져와 리스트 만들기
# - <Step2. 한글 추출> - 정규식을 이용하여 한글과 띄어쓰기만 가져오기
# - <Step3. 말뭉치 만들기> - join() 함수로 리스트를 말뭉치로 만들기
# - <Step4. 명사 추출 및 빈도수 계산> - 코엔엘파이(konlpy)를 이용한 형태소 분섣으로 명사만 추출하기
# - <Step5. 키워드 만들기> - 2글자 이상만 저장
# - <Step6. 불용어 제거> - 실질적인 의미가 없는 키워드 처리
# - <Step7. 워드 클라우드 시각화> pytagcloud, wordcloud, pilow 라이브러리를 활용한 워드 클라우드 시각화

# ## <Step1. 웹 크롤링>
# ### 크롤링으로 웹 데이터 가져오기
# ---
# **[웹 크롤링 라이브러리 사용하기]**
# - 파이썬에서는 Beautifulsoup과 requests 라이브러리로 웹 크롤러를 생성
# - requests는 특정 URL로부터 HTML 문서를 가져오는 작업 수행
# - 나무위키와 같은 페이지는 HTML 문서가 JavaScript로 동적 로딩되는 경우가 있음
# - requests 대신 셀레니움(selenium) 라이브러리를 이용해 크롬 브라우저로 동적 웹 크롤링
# - selenium은 웹 브라우저를 자동으로 구동
# - selenium을 사용하기 위해 크롬 드라이버를 이용해 브라우저 자동 구동 => 드라이버 필요

# +
#pip install selenium beautifulsoup4 requests

# +
import pyautogui as pya
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

import re # 정규식 표현을 위한 모듈
import time
import warnings
warnings.filterwarnings("ignore")

# +
keyword = pya.prompt("검색어를 입력하세요.")
lastpage = int(pya.prompt("마지막 페이지 번호를 입력하세요."))

# 뉴스 제목(text)를 담을 리스트
titleList = []

# NAVER 뉴스 URL로부터 응답 요청, 사용자로부터 입력받은 변수값 적용
# fstring (f"문자열{변수}")
for i in range(1, lastpage*10, 10) :
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start=[i]")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # select 경로를 통한 검색
    # title = soup.select("div.news_wrap.api_ani_send > div > a")
    # class를 통한 검색
    titles = soup.select("a.news_tit")
    subtitles = soup.select("a.elss.sub_tit")
    
    for title in titles : # titles에서 title
        titleText = title.text # title.text만 추출
        titleList.append(titleText) # titleList에 추가
        
print(titleList)


# -

# ## <Step2. 한글 추출>
# ### [텍스트 데이터 전처리]<br>정규식 사용하여 한글과 띄어쓰기만 가져오기
# ---
# **파이썬 정규 표현식(re) 사용법 - 05. 주석, 치환, 분리**
# - 정규 표현식: 컴파일 => re.compile, 미리 컴파일해두고 저장
# - 정규 표현식: 치환 => re.sub(pattern, repl, string, count, flags)

# +
# 한글 코드 범위
# ㄱ-ㅎ
# ㅏ-ㅣ
# 가-힣
# [^ ㄱ-ㅣ가-힣]+ 한글과 띄어쓰기 정규식 패턴(띄어쓰기 주의)

# 사용자 정의 함수 선언
def text_cleaning(text) :
    # 한글과 띄어쓰기를 제외한 모든 글자 패턴을 지정하여 hangul로 정의
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    # 한글과 띄어쓰기를 제외한 모든 글자 패턴을 공백으로 치환
    result = hangul.sub('', text)
    return result

text_cleaning(titleList[1])

# +
# lambda 함수:return없이 수행되는 함수 => 함수의 인자로 함수를 받음
# lambda 인자(arfuments):식(expression)
# 간단한 함수를 대신할 수 있으며, filter()나 map() 함수의 인자로 많이 사용
# filter(), map() => list() 함수와 함께 사용
# filter()는 특정 조건에 해당하는 값만 리턴, map()은 리스트에 함수 적용

# titleList에 데이터 전처리 적용
# titleList의 한글과 띄어쓰기를 제외한 모든 부분을 제거하고 덮어쓰기
titleList = list(map(lambda x:text_cleaning(x), titleList))
titleList
# -

# ## <Step3. 말뭉치 만들기>
# ### join() 함수로 리스트를 말뭉치로 만들기
# ---

title_corpus = " ".join(titleList)
title_corpus

# ## <Step4. 명사 추출 및 빈도수 계산>
# ### 코엔엘파이(konlpy)를 이용한 형태소 분석으로 명사만 추출하기
# ---
# ### [코엔엘파이(konlpy)를 이용한 형태소 분석]
# - 품사란 단어를 기능, 형태, 의미에 따라 나눈 갈래
# - 우리나라 학교 문법에서는 명사, 대명사, 수사, 조사, 동사, 형용사, 관형사, 부사, 감탄사의 9가지로 분류
#
# ### [형태소 분석과 품사 태깅]
# - 형태소 : 더 이상 분리를 할 수 없는 의미를 갖는 최소 단어를 의미
# - 형태소 분석 : 형태소를 비롯하여, 어근, 접두사/접미사, 품사(POS, part-of-speech) 등 다양한 언어적 속성의 구조를 파악하는 것
# - 품사 태깅 : 형태소와 품사를 매칭시키는 것
#
# ### [빈도 분석: 문장 형태소 분석 - koNLPy]
# - koNLPy : 파이썬 한국어 형태소 분석 라이브러리

# +
# # !pip install konlpy
# -

import sys
sys.version

import konlpy
from konlpy.tag import Okt
from collections import Counter

# konlpy의 형태소 분석기로 타이틀 말뭉치에서 명사 단위의 키워드를 추출한 후 명사의 빈도수 계산
# 명사 단위 키워드 추출
nouns_tagger = Okt()
# nouns() 함수를 이용하여 title_corpus 문장 중 명사만 추출
nouns = nouns_tagger.nouns(title_corpus)
count = Counter(nouns) # 각 명사의 빈도수 계산

# ## <Step5. 키워드 가다듬기>
# ### 2글자 이상만 저장하기
# ---

# 한글자 키워드를 제거한 후 내림차순 정렬
# x는 키, count[x] 값으로 키의 값이 2 이상일 경우에만 remove_char_counter에 저장
remove_char_counter = Counter({x:count[x] for x in count if len(x) > 1})
print(remove_char_counter)

# ## <Step6. 불용어 제거하기>
# ### 실질적인 의미가 없는 불용어 제거하기
# ---
# - 실질적인 의미가 없는 키워드 처리
# - 관사나 접속사 등 실질적인 의미가 없으면서 동시에 의미적인 독립을 할 수 없는 품사 제거
# - **[한국어 약식 불용어사전 예시 파일]**<br>
# 출처 - (https://www.ranks.nl/stopwords/korean)
# - 인터넷 검색 시 검색 용어로 사용하지 않는 단어
# - 관사, 전치사, 조사, 접속사 등은 검색 색인 단어로 의미가 없는 단어
# - 각 검색 엔진마다 그 내용은 다를 수도 있음

# +
korean_stopwords_path = "korean_stopwords.txt"

# 텍스트 파일을 오픈
# 불용어 텍스트 파일을 열어 f로 치환
with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines() # 파일로부터 불용어를 한 줄씩 읽어들임
# 리스트 생성, strip() 함수는 공백, 줄바꿈, tab 등을 모두 제거
stopwords = [x.strip() for x in stopwords]
#print(stopwords[:10]) # 리스트 출력
print(stopwords) # 리스트 출력
# -

# 네이버 페이지에 맞는 불용어를 추가
namu_wiki_stopwords = ['상위', '문서', '내용', '누설', '아래', '해당', '설명',
                       '표기', '추가', '모든', '사용', '매우', '가장', '줄거리',
                       '요소', '상황', '편집', '틀', '경우', '때문', '모습',
                       '정도', '이후', '사실', '생각', '인물', '이름', '년월']
# 네이버 불용어를 기존 불용어 사전에 하나씩 추가
for stopword in namu_wiki_stopwords: 
    stopwords.append(stopword)
stopwords

# +
# 키워드 데이터에서 불용어를 제거
# Counter는 각 명사의 빈도수를 계산하여 딕셔너리 형태로 반환
# x는 키, remove_char_counter[x] 값으로 x는 키워드,
## remove_char_counter[x]는 빈도수
# 기존 한글자 키워드를 제거한 content_corpus의 키워드에서
## 불용어 사전에 있지 않은 키워드만 remove_char_counter에 저장
remove_char_counter = Counter({x : remove_char_counter[x] for x in count if x not in stopwords})

# 한글자 키워드를 제거 후 내림차순 정렬
# x는 키, count[x] 값으로 키의 값이 2이상일 경우만 remove_char_counter에 저장
remove_char_counter = Counter({x : count[x] for x in count if len(x) > 1})
print(remove_char_counter)
# -

# ## < Step7. 워드클라우드 시각화> 
# ### pytagcloud, wordcloud, pillow 라이브러리를<br>활용한 워드 클라우드 시각화
# ---
# **[pytagcloud 사용하기]**
#
# - 1) 아래 코드 실행을 위해, anaconda prompt 혹은 Terminal에서 아래와 같은 패키지들을 설치
# - pip install pytagcloud pygame simplejson
# - 2) 한글 폰트(예: NanumBarunGothic.ttf) 파일 지정
# - Windosw OS : {anaconda_path}\envs{env_name}\Lib\site-packages\pytagcloud\fonts
#   - C:\Users\사용자명\anaconda3\Lib\site-packages\pytagcloud\fonts
# - 한글 나눔글꼴 다운로드 http://hangeul.naver.com/webfont/NanumGothic/NanumGothic.ttf
# - 파일을 옮긴 후, 파이썬 가상환경을 재실행 하여 주피터를 다시 실행
# - 3) 위 방법으로 한글 폰트가 지정이 안될 경우 다음 방법으로 한글 폰트 지정
#     - 위의 경로에서 font.json 파일을 편집합니다.
#     - 아래와 같은 코드를 추가하고 font.json 파일을 저장합니다.
#     - {
#                 "name": "NanumGothic",
#                 "ttf": "NanumGothic.ttf",
#                 "web": "http://fonts.googleapis.com/css?family=Nanum+Gothic"
#     - },

# !pip install pytagcloud pygame simplejson

# +
import random
import pytagcloud
import webbrowser

# 가장 출현 빈도수가 높은 40개의 단어를 선정
ranked_tags = remove_char_counter.most_common(40)

# pytagcloud로 출력할 40개의 단어를 입력. 단어 출력의 최대 크기는 80으로 제한
taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)

# pytagcloud 이미지로 워드 클라우드 생성. 폰트는 나눔 고딕을 사용
pytagcloud.create_tag_image(taglist, 'wordcloud_content.jpg',
                            size=(900, 600), fontname='NanumGothic',
                            rectangular=False)
ranked_tags

# +
# 생성한 이미지를 주피터 노트북상에서 출력
from IPython.display import Image

##### 제목 키워드 시각화

# pytagcloud 이미지를 생성. 폰트는 나눔 고딕을 사용
# pytagcloud.create_tag_image(taglist, 'wordcloud_heart.jpg'
# size=(900, 600), fontname='NanumGothic', rectangular=False) 
pytagcloud.create_tag_image(taglist, 'wordcloud_title.jpg', size=(900, 600), fontname='NanumGothic', rectangular=False) 
Image(filename='wordcloud_title.jpg') # 생성한 이미지를 주피터 노트북상에서 출력
# -

# ### [wordcloud 와 pillow를 이용한 워드 클라우드 시각화]
# - https://doitgrow.com/34
# - https://github.com/amueller/word_cloud
#
# #### < 1. wordcloud 설치 >
# - 콘다 프롬프트에서 아래 명령어 실행
# - conda install -c conda-forge wordcloud
#    
# #### < 2. pillow 설치 >
# - pip install pillow

# !pip install pillow
# !pip install wordcloud

# +
# -*- coding: utf-8 -*-

from PIL import Image
from wordcloud import WordCloud

wc = WordCloud(font_path='NanumGothic', width=1200, height=1200,
               scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(remove_char_counter)

plt.figure()
plt.imshow(gen)
plt.axis('off')  # 축 설정
plt.savefig('wordcloud.jpg') # 워드 클라우드 저장

# +
# 블랙 이미지의 jpg나 png 파일을 마스크로 적용
img = Image.open('wordcloud_heart.jpg')
img_array = np.array(img)

wc = WordCloud(font_path='malgun', width=1200, height=1200, scale=4.0, 
               max_font_size=250, mask=img_array, background_color = "white")
gen = wc.generate_from_frequencies(remove_char_counter)

plt.figure()
plt.imshow(gen)
plt.axis('off')                          # 축 설정
plt.savefig('wordcloud_heart_save.jpg')       # 워드 클라우드 저장
