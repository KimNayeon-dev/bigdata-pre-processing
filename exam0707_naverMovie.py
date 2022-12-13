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

# ## <네이버 영화 사이트 크롤링 후 시각화>
# ### 네이버 영화 사이트 '상영작', '예정작' 크롤링
# ---
# > - 네이버 영화 제목, 네티즌 별점 점수 크롤링하여 예매순 상위 10개 출력하기
# > - 예매순 순위 10개의 별점 점수에 대해 그래프로 시각화하기
# > - 예매순 상위 10개의 별점 점수 중 가장 높은 영화의 그래프를 색상으로 강조하기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
# %matplotlib inline

response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220707")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
soup

# +
title = soup.select("td.title > div > a")
point = soup.select("td.point")

print(title)
print(point)

# +
movieTitle = [] # 영화 제목 리스트
moviePoint = [] # 영화 평점 리스트

for i in range(0, 10, 1) :
    print("%d. "%(i+1)+title[i].text, "/ 별점 => "+point[i].text)
    movieTitle.append(title[i].text) # i번째 title.text를 movieTitle 리스트에 추가
    moviePoint.append(point[i].text) # i번째 point.text를 moviePoint 리스트에 추가
# -

movieSet = list(zip(movieTitle, moviePoint)) # movieTitle과 moviePoint를 묶어 movieSet 생성
movieDf = pd.DataFrame(movieSet) # 데이터 프레임 생성
movieDf.columns=["Title", "Point"]
movieDf["Point"] = movieDf["Point"].apply(lambda x:float(x))
movieDf

plt.rc("font", family="Malgun Gothic", size=14, weight='light') # 그래프에 한글 폰트 입력
x = movieDf["Title"]
y = movieDf["Point"]
plt.figure(figsize=(6, 6))
plt.bar(x, y)
plt.bar(x, y)[movieDf["Point"].idxmax()].set_color('royalblue')
plt.ylabel('평점', size=20, weight='bold')
plt.title('네이버 영화순위 및 평점', size=24, weight='bold')
plt.xticks(rotation=90)
for i in range(len(x)) :
    plt.text(x[i], y[i], y[i], size=12,
         horizontalalignment='center', verticalalignment='bottom')
plt.show()
