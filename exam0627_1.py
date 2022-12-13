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

# ## [웹크롤링 실습]
# ---
# - NAVER에서 '코로나' 키워드로 검색한 최신 뉴스 10개의 제목과 UTL 주소 크롤링해서 출력하기
# - DAUM에서 '코로나' 키워드로 검색한 최신 뉴스 10개의 제목과 UTL 주소 크롤링해서 출력하기

# +
import requests
from bs4 import BeautifulSoup

# 특정 주소 naver 서버에 대화를 시도
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98")

# naver 에서 HTML 가져옴
html = response.text

# html.parser(html 번역기로 해석)
soup = BeautifulSoup(html, 'html.parser')

# HTML 출력
print(soup)
# -

title = soup.select("div.news_wrap.api_ani_send > div > a")
print(title)

for title_one in title :
    print(title_one.text, "=>", title_one.attrs['href'])

# +
# 특정 주소 daum 서버에 대화를 시도
response = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EB%A1%9C%EB%82%98")

# daum 에서 HTML 가져옴
html = response.text

# html.parser(html 번역기로 해석)
soup = BeautifulSoup(html, 'html.parser')

# HTML 출력
print(soup)
# -

title = soup.select("div.wrap_cont > a")
print(title)

for title_one in title :
    print(title_one.text, "=>", title_one.attrs['href'])
