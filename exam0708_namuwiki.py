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

# ## <웹 크롤링 - 나무위키 사이트 분석 및 시각화>
# ---
# ### <Step1. 크롤링> : 크롤링으로 웹 데이터 가져오기
# > **[웹 크롤링 라이브러리 사용하기]**
# > - 파이썬에서는 BeautifulSoup과 requests라는 라이브러리로 웹 크롤러를 만들 수 있음
# > - requests는 특정 URL로부터 HTML 문서를 가져오는 작업을 수행
# > - 나무위키와 같은 페이지는 HTML 문서가 JavaScript로 동적 로딩되는 경우가 있음
# > - requests 대신 셀레니움(selenium) 라이브러리를 이용해 크롬 브라우저로 동적 웹 크롤링 수행
# > - selenium은 웹 브라우저를 자동으로 구동해주는 라이브러리
# > - selenium을 사용하기 위해 크롬 드라이버를 이용해 크롬 브라우저 자동으로 구동 => 크롬 브라이버 필요
#
# ### [BeautifulSoup 과 selenium을 이용한 웹 크롤링]
# > - anadonda prompt 혹은 Terminal에서 아래와 같은 패키지들을 설치
# > - (env_name) pip install selenium
# > - (env_name) pip install beautifulsoup4
#
# ### [크롬 브라우저 업데이트 및 크롬 드라이버 설치]
# > - 크롬 브라우저 설정에서 최신 버전으로 업데이트
# > - 크롬 드라이버 사이트에서 브라우저 버전에 맞는 드라이버 다운로드
# > - https://chromedriver.chromium.org/downloads
# > - chromedriver.exe 파일을 노트북 파일 경로에 이동

# +
# #!pip install selenium beautifulsoup4

# +
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import re # 정규식 표현을 위한 모듈

import warnings # 실행 상 문제없는 문제 무시
warnings.filterwarnings("ignore")

# +
# 윈도우용 크롬 웹드라이버 실행 경로 (Windows) 지정
executable_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)

# 사이트의 html 구조에 기반하여 크롤링을 수행
source_url = "https://namu.wiki/RecentChanges" # 크롤링할 사이트 주소를 정의
driver.get(source_url)  # 크롬 드라이버를 통해 URL의 HTML 문서 가져옴

import time
time.sleep(10)

req = driver.page_source
soup = BeautifulSoup(req, "html.parser") # BeautifulSoup의 soup 객체로 변환

table_rows = soup.select("table tbody tr")
# -

table_rows

# ### [페이지 링크 주소 리스트 가져오기]
# ---

# +
page_url_base="https://namu.wiki" # 베이스 URL 정의
page_urls = [] # href 속성값을 담기 위한 빈 리스트 생성

for index in range(0, len(table_rows)) :
    first_td = table_rows[index].find_all("td")[0]
    td_url = first_td.find_all("a")
    
    if len(td_url) > 0 :
        page_url = page_url_base + td_url[0].attrs["href"]
        if "png" not in page_url :
            page_urls.append(page_url)
print(page_urls)
# -

page_urls[0]

# ### [각 링크 페이지 내 텍스트 구조를 확인하여 제목, 카테고리, 내용 출력]
# ---

# +
# 크롬 드라이버를 통해 page_urls[0]번째 사이트의 HTML 문서를 가져옴
driver.get(page_urls[0]) # page_urls[0]의 정보를 가져옴
req = driver.page_source # 페이지 소스를 req에 저장
soup = BeautifulSoup(req, 'html.parser') # html.parser로 파싱

# 타이틀(h1) 추출
title = soup.select_one("h1")

# 카테고리 추출
category = soup.select_one("div._8DgSHiLA~ul") # div의 _8DgSHiLA 클래스부터(~) ul

# 내용 추출
content_paragraphs = soup.select_one("div.HMXdAcwv") # div의 HMXdAcwv 클래스
# -

print(title.text)
print(category.text)
print()
print(content_paragraphs.text)
