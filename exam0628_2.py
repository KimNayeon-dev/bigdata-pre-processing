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

# ## <빅데이터분석_공공데이터포털활용>
# ### 공공데이터포털 사이트의 데이터를 수집하여 빅데이터 분석 및 시각화하기
# ---
# > - 인사이트 도출을 위한 특정 주제를 선정하기
# > - 공공데이터포털(https://www.data.go.kr/)에서 관련 파일 데이터(*.csv) 수집하기
# > - 수집한 데이터를 이용하여 데이터 분석 후 인사이트 도출하기
# > - 분석한 데이터를 시각화하기
#
# **[제출형식]**<br>
# 주피터 노트북(*.ipynb), 수집한 파일 데이터(*.csv), 결과 PDF파일<br>
# \> 본인 명의 폴더를 생성하여 제출할것

import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt

data2019 = pd.read_csv('../examData/경기도 성남시_반려동물_등록현황_20191014.csv', encoding='cp949')
data2020 = pd.read_csv('../examData/경기도 성남시_반려동물_등록현황_20200531.csv', encoding='cp949')
data2021 = pd.read_csv('../examData/경기도 성남시_반려동물_등록현황_20210430.csv', encoding='cp949')

# ## "우리나라는 정말 <span style="color:salmon">반려동물 천만시대</span>일까?"
# # 도시별 반려동물 등록수 변화(2019-2021년)
# ---
# - **<span style="color:orange">[2021년 반려동물 등록수] >> 주황색</span>**
# - **<span style="color:#6699ff">[2020년 반려동물 등록수] >> 하늘색</span>**
# - **<span style="color:#5cd1e5">[2019년 반려동물 등록수] >> 연하늘색</span>**

# +
plt.rc("font", family="Malgun Gothic", size=14)

plt.figure(figsize=(10, 6))

plt.bar(data2021["읍면동(법정동)"][11:15], data2021["합계"][11:15], color='lightyellow')
plt.plot(data2019["읍면동(법정동)"][11:15], data2019["합계"][11:15], linewidth=3, color='lightblue')
plt.scatter(data2019["읍면동(법정동)"][11:15], data2019["합계"][11:15], s=100, color='lightblue')
plt.plot(data2020["읍면동(법정동)"][11:15], data2020["합계"][11:15], linewidth=3, color='#6699ff')
plt.scatter(data2020["읍면동(법정동)"][11:15], data2020["합계"][11:15], s=100, color='#6699ff')
plt.plot(data2021["읍면동(법정동)"][11:15], data2021["합계"][11:15], linewidth=3, color='orange')
plt.scatter(data2021["읍면동(법정동)"][11:15], data2021["합계"][11:15], s=100, color='orange')

plt.ylabel("반려동물 등록수", size=18, weight='bold')
plt.title("경기도 성남시", size=30, weight='bold')

plt.show()
# -

data2019 = pd.read_csv('../examData/인천광역시 부평구_반려동물 등록현황_20191015.csv', encoding='cp949')
data2021 = pd.read_csv('../examData/인천광역시 부평구_반려동물 등록현황_20211110.csv', encoding='cp949')

# +
plt.figure(figsize=(9, 6))

plt.bar(data2021["법정동명"][2:7], data2021["등록동물수"][2:7], color='lightyellow')
plt.plot(data2019["법정동명"][2:7], data2019["등록동물수"][2:7], linewidth=3, color='lightblue')
plt.scatter(data2019["법정동명"][2:7], data2019["등록동물수"][2:7], s=100, color='lightblue')
plt.plot(data2021["법정동명"][2:7], data2021["등록동물수"][2:7], linewidth=3, color='orange')
plt.scatter(data2021["법정동명"][2:7], data2021["등록동물수"][2:7], s=100, color='orange')

plt.ylabel("반려동물 등록수", size=18, weight='bold')
plt.title("인천광역시 부평구", size=30, weight='bold')

plt.show()
# -

data2019 = pd.read_csv('../examData/서울특별시_관악구_반려동물 등록현황_20191010.csv', encoding='cp949')
data2021 = pd.read_csv('../examData/서울특별시_관악구_반려동물 등록현황_20210222.csv', encoding='cp949')

# +
plt.figure(figsize=(9, 6))

plt.bar(data2021["읍면동명"], data2021["등록동물수"], color='lightyellow')
plt.plot(data2019["법정동명"], data2019["등록동물수"], linewidth=3, color='lightblue')
plt.scatter(data2019["법정동명"], data2019["등록동물수"], s=100, color='lightblue')
plt.plot(data2021["읍면동명"], data2021["등록동물수"], linewidth=3, color='orange')
plt.scatter(data2021["읍면동명"], data2021["등록동물수"], s=100, color='orange')

plt.ylabel("반려동물 등록수", size=18, weight='bold')
plt.title("서울특별시 관악구", size=30, weight='bold')

plt.show()
# -

# ---
# ## 최근 3년간 반려동물 등록수는 <span style="color:salmon"><상승세></span>
# **유기동물 발생수도 <span style="color:darkred"><상승세>...**<br>
# **펫샵 사업체수도 <span style="color:darkred"><상승세>...**
# ---
