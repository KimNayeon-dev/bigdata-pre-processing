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

# ## [크롤링 기초] 크롤링을 위한 HTML 및 CSS 선택자
# ---
# - **크롤링**을 위한 HTML - 뉴스 해킹
# - HTML을 파이썬으로 가져오기 : `requests`
# > `!pip install requests`
# - 원하는 태그 선택하기 : `beautifulsoup`
# > `!pip install beautifulsoup4`
# - **크롤링**에서 가장 중요한 CSS 선택자
# ---

# !pip install requests

# !pip install beautifulsoup4

# +
# HTML을 파이썬으로 가져오기 : requests
# 원하는 태그 선택하기 : beautifulsoup
import requests
from bs4 import BeautifulSoup

# 특정 주소 naver 서버에 대화를 시도
response = requests.get("https://www.naver.com")

# naver 에서 HTML 가져옴
html = response.text

# html.parser(html 번역기로 해석)
soup = BeautifulSoup(html, 'html.parser')

# HTML 출력
print(soup)
# -

# select는 모든 태그 선택, select_one은 하나의 태그만 선택
# id 값이 NM_set_home_btn인 것을 찾아냄
# select("CSS선택자")
word = soup.select_one("#NM_set_home_btn")

# find("태그명")
# find(class_="classname")
# find(id=""idname)
word = soup.find(id="NM_set_home_btn")

# word에서 텍스트 요소만 출력
print(word.text)

# 모든 속성과 속성값을 데이터프레임 형태로 출력
print(word.attrs)

# 특정 속성값만 추출하기
print(word.attrs['href'])

# div.title_area > strong 클래스 속성을 가진 read 추출
read = soup.select_one("div.title_area > strong")
# read에서 text만 출력
print(read.text)

word = soup.select("strong")
for word_one in word :
    print(word_one, word_one.text)
