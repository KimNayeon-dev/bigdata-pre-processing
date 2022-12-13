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
# - NAVER 뉴스에서 여러 페이지 크롤링하여 출력하기

# +
import requests
from bs4 import BeautifulSoup

pageNum = 1

for i in range(1, 100, 10) :
    # 특정 주소 naver 서버에 대화를 시도
    # fstring f"문자열[변수명]"
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=[i]")

    # naver 에서 HTML 가져옴
    html = response.text

    # html.parser(html 번역기로 해석)
    soup = BeautifulSoup(html, 'html.parser')

    # select 부분
    title = soup.select("div.news_wrap.api_ani_send > div > a")
    
    # for문 반복 출력 부분
    for title_one in title :
        print(title_one.text, "=>", title_one.attrs['href'])
        
    print("-------------------------------", pageNum, "page -------------------------------")
    pageNum += 1
