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

# ## NAVER 영화 랭킹 TOP10 제목만 가져오기
# ---

# +
import requests
from bs4 import BeautifulSoup

# 특정 주소 naver 서버에 대화를 시도
response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")

# naver 에서 HTML 가져옴
html = response.text

# html.parser(html 번역기로 해석)
soup = BeautifulSoup(html, 'html.parser')

# HTML 출력
print(soup)
# -

movie = soup.select("td.title > div > a")
print(movie)

for i in range(0, 10, 1) :
    print("%d. "%(i+1)+movie[i].text)
