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

# ## [Pandas, Numpy, Matplotlib] 실습
# ---
# ### 판다스(Pandas)
# > - 파이썬에서 가장 널리 사용되는 데이터 분석 라이브러리로<br>
# '데이터 프레임' 이라는 자료구조 이용
# > - 데이터 프레임은 엑셀의 스프레드 시트와 유사한 형태,<br>
# 파이썬으로 데이터를 쉽게 처리할 수 있도록 함

# 판다스 라이브러리 불러오기
import pandas as pd

# +
# 데이터 프레임 생성하고 일부분 살펴보기
# 판다스의 데이터 프레임을 생성
# 데이터 프레임에 들어갈 2개의 열 데이터 입력
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
gender = ['male', 'female', 'female', 'male', 'male']

# list(), zip() 함수로 데이터셋 생성 / BabyDataSet에 저장
BabyDataSet = list(zip(names, births, gender))

# pd.DataFrame()을 통해 데이터셋으로 데이터 프레임 객체 생성 / df에 저장
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births', 'Gender'])

# 데이터 프레임(df)의 상단 4개 출력 / df.tail(4) # 하단 4개 출력
df.head(4)
# -

# 데이터 프레임의 열 타입 정보를 출력
df.dtypes

# 데이터 프레임의 인덱스 정보를 출력
df.index

# 데이터 프레임 열의 형태 정보를 출력
df.columns

# 데이터 프레임에서 하나의 열을 선택
df['Births']

# 2~4번째 인덱스를 선택
df[2:4]

# +
# Births 열이 100보다 큰 데이터를 선택
# df[df['Births'] > 100]

# Gender 열이 male인 데이터를 선택
df[df['Gender'] == 'male']
# -

# 데이터 프레임에서의 평균값 계산
df.mean()

# 데이터 프레임에서의 최대값 계산
df.max()

# 데이터 프레임의 모든 값을 더해줌
df.sum()

# ---
# ### 넘파이(Numpy)
# > - 수치 계산을 위해 만들어진 파이썬 라이브러리
# > - 넘파이의 자료 구조는 판다스 라이브러리, Matplotlib의 기본 데이터 타입으로 사용
# > - 넘파이는 배열 개념으로 변수를 사용하여 벡터, 행렬 등의 연산을 쉽고 빠르게 수행

import numpy as np

# 넘파이 배열 선언, 파이썬의 기본 자료구조 배열과는 다른 데이터 타입
# 1차원 배열 생성
# array() 함수는 리스트를 직접 넣어 배열 생성
# arange() 함수는 파이썬의 range() 함수와 같이 원하는 함수의 배열을 만듦
# 0에서부터 15까지 배열 생성 = np.arange(0, 15)
arr1 = np.arange(15)
arr1

# array() 배열 생성
# Numpy 형식으로 배열의 원소를 입력할 때는 반드시 리스트 형식으로 입력
np.array([1, 3, 4, 6])

# reshape() 원하는 모양의 다차원 배열을 생성
arr2 = np.arange(15).reshape(3, 5)
arr2

# 생성한 데이터의 차원 확인
arr2.shape

# 생성한 데이터의 변수 타입 확인
arr1.dtype

# 3X4 2차원 넘파이 배열 생성
arr3 = np.zeros((3, 4))
arr3

# 5개의 1차원 넘파이 배열 생성
arr3 = np.zeros(5)
arr3

# 10개의 1차원 넘파이 배열 생성(ones)
arr3 = np.ones(10)
arr3

arr4 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
arr4

arr5 = np.array([[7, 8, 9], [10, 11, 12]], dtype=np.float64)
arr5

# 배열 간의 사칙 연산
arr4+arr5

arr4-arr5

arr4*arr5

arr4/arr5

# ---
# ### 맷플롯립(Matplotlib)
# > - 데이터를 시각화해주는 가장 기본적인 라이브러리

import matplotlib.pyplot as plt

# +
# https://matplotlib.org/stable/index.html
plt.style.use('_mpl-gallery-nogrid')


# make data
x = [1, 2, 3, 4, 5]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=7, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
# -

# ---
# ### 맷플롯립(Matplotlib)의 활용

# 주피터 노트북에서 matplotlib를 통해 시각화된 그래프를 출력하기 위해
# 코드를 미리 실행해두어야 함
# 현재 실행 중인 주피터 노트북에서 그래프를 출력 가능하도록 선언하는 명령어
# %matplotlib inline
import matplotlib.pyplot as plt

# +
# 막대 그래프 출력
x = df['Names'] # x 축의 값으로 사용할 시리즈를 변수 x 값으로 지정
y = df['Births'] # y 축의 값으로 사용할 시리즈를 변수 y 값으로 지정

plt.bar(x, y)
plt.plot(x, y, linewidth=3, color='orange')
plt.scatter(x, y)

# 각 축의 이름(라벨)
plt.xlabel('Baby Names')
plt.ylabel('Baby Births')

# 그래프의 제목
plt.title('Bar Plot')

plt.show()
