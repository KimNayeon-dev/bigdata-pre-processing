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

# ## NAVER 서버에서 뉴스 제목만 가져오기
# ---

# +
import requests
from bs4 import BeautifulSoup

# 특정 주소 naver 서버에 대화를 시도
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1")

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
    print(title_one.text)

for title_one in title :
    print(title_one.attrs['href'])
