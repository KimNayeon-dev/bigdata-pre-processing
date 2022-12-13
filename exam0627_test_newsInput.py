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

# ## [실전 프로젝트]
# ### 뉴스 데이터 수집하기 / 검색어에 따라 다른 결과 나타내기
# ---
# - **URL의 개념 : 인터넷 주소 형식**
# - 프로토콜, 도메인, 패스(경로),<br>
# 파라미터(서버의 추가적인 정보를 제공하기 위해서 사용, 키와 값으로 구성, &로 구분)
# - query는 검색어에 해당됨
# - 파이썬에서 사용자에게 검색어를 입력받은 뒤 query 값에 적용하면 검색어 변경 가능

# +
import requests
from bs4 import BeautifulSoup
import pyautogui

pageNum = 1

# 파이썬 기본 내장 함수 input으로 사용자로부터 검색어를 입력받음
keyword = input("검색어를 입력하세요.")
lastPage = int(input("마지막 페이지 번호를 입력하세요."))

for i in range(1, lastPage*10, 10) :
    # 특정 주소 naver 서버에 대화를 시도
    # fstring f"문자열[변수명]"
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword+"&start=[i]")

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
