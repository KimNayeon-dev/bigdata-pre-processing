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

# ## [웹크롤링 퀴즈]
# ### daum 실시간영화예매율 / 일간영화순위 크롤링하여 출력하기
# ---
# - 다음 영화 사이트에서 사용자의 입력 값에 따라 실시간 예매율과<br>
# 일간 순위 리스트를 각각 출력할 것
# - 이때 입력창은 pyautogui 모듈을 활용할 것
# - 실시간 예매율은 1, 일간순위 리스트는 2 값으로 입력받을 것
# - 1 또는 2 외의 값이 들어오면 계속 입력창을 띄워 입력받을 것

# +
import requests
from bs4 import BeautifulSoup
import pyautogui as pya

while(True) :
    keyword = int(pya.prompt("실시간영화예매율은 1, 일간영화순위는 2를 입력해주세요."))
    
    if(keyword==1) :
        response = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=영화")
        break
    elif(keyword==2) :
        response = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=일간영화순위")
        break
    else :
        continue

# response = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=영화")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# select 부분
title = soup.select("div.wrap_cont.cont_type2 > div")

# 영화순위 반복출력 부분
for i in range(0, 29, 1) :
    print("%d. "%(i+1)+title[i].text)
# -


