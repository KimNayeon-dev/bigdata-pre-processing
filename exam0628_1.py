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

# ## 멕시코풍 프랜차이즈 Chipotle의 주문 데이터 분석하기
# ---
# ### <Step1. 탐색> : 데이터의 기초 정보 살펴보기
# > - Chipotle 데이터셋의 기본 정보
# > - Chipotle 데이터셋의 행과 열, 데이터
# > - Chipotle 데이터셋의 수치적 특징 파악

import pandas as pd

# 데이터를 불러온 뒤, 불러온 데이터 구성 정보를 출력하는 코드
# read_csv 함수로 데이터를 Dataframe 형태로
# csv(comma separated value)는 쉼표 기준,
# tsv(tab separated value)는 tab 기준으로 항목을 구분하여 저장한 데이터
file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')

# 데이터 프레임의 행과 열의 정보 출력 / print()는 생략 가능
print(chipo.shape)

chipo.info()

# chipo라는 Dataframe에서 순서대로 10개의 row 데이터를 출력
chipo.head(10)

# columns() 함수로 컬럼의 정보를 보여줌
# order_id : 주문 번호
# quantity : 주문 수량
# item_name : 주문한 상품명
# choice _description : 주문 아이템의 상세 선택 옵션
#item_price : 주문한 상품가격
chipo.columns

# index는 인덱스 정보
chipo.index

# ---
# ### <Step2. 인사이트의 발견> : 탐색과 시각화
# > - 가장 많이 주문한 item
# > - item당 주문 개수와 총량 구하기
# > - 시각화로 분석 결과 살펴보기

# Chipotle 데이터셋의 수치적 특징 파악
# describe() 함수로 요약 통계량 출력하기(수치적 계산이 가능한 피처만 출력)
# chipo dataframe에서 수치형 피처들의 요약 통계량을 확인
# 데이터의 count(수), mean(평균), std(표준편차), min(최소값),
# 25%(1사분위수), 50%(2사분위수), 75%(3사분위수), max(최대값)
chipo.describe()

chipo.mean()

# astype() 함수로 order_id의 데이터 타입을 String으로 변경
# 수치형이 아니므로 숫자의 의미를 가지지 않아 결과에서 제외됨
chipo['order_id'] = chipo['order_id'].astype(str)
chipo.describe()

# ---
# ### unique() 함수로 범주형 피처의 개수 출력하기

# unique() 함수는 열(시리즈)의 중복값을 제거한 고유값만 출력
# order_id와 item_name의 피처 형태 특징 - 범주형 피처
# len(chipo['피처명'].unique())는 열(시리즈)의 고유값 수
print(chipo['order_id'].unique())
print(len(chipo['order_id'].unique()))

print(chipo['item_name'].unique())
print(len(chipo['item_name'].unique())) # 길이

# ---
# ### [가장 많이 주문한 item]

# +
# Dataframe['column'] 형태에 value_counts() 함수 적용

# 가장 많이 주문한 item:top10을 출력
# value_counts() 각 원소의 빈도수 출력, 시리즈 객체에만 적용
# Series(시리즈)는 복수의 행(row)으로 이루어진 하나의 열(column) 구조
chipo['item_name'].value_counts()[5:10] # 상위 5위에서 10위까지
# -

chipo['item_name'].value_counts()[:10] # 상위 10개

# ---
# ### [item당 주문 개수]

# +
# groupby() 함수는 데이터 프레임에서 특정 피처를 기준으로
# 그룹을 생성하여, 이를 통해 그룹별 연산을 적용

print("[COUNT]")
print(chipo.groupby('item_name')['quantity'].count()[:10])
print()

print("[SUM]")
# item_name으로 그룹 지어진 피처의 quantity의 합(sum)을 구함
print(chipo.groupby('item_name')['quantity'].sum()[:10])
# -

chipo.groupby('item_name')['item_price'].sum()[:10]

# ---
# ### <Step3. 데이터 전처리> : 전처리 함수 사용하기
# > - apply()와 lambda를 이용해 데이터 전처리하기

# +
print("[ITEM_PRICE]")
print(chipo['item_price'])
print()

print("[ITEM_PRICE_LAMBDA]")
# column 단위 데이터에 apply 함수로 전처리를 적용

# apply() 함수는 시리즈 단위의 연산을 처리하는 기능을 수행하여
# sum()이나 mean()과 같이 연산이 정의된 함수를 파라미터로 받음

# lambda 뒤에 나오는 인수는 함수에서 사용될 변수 x를 정의하며,
# 변수를 실수형으로 변환하는 float 함수에 적용시킨 결과를 x에 다시 대입

# lambda 함수는 문자열 데이터에서 첫번째 문자열을 제거한 뒤
# 1번째부터 나머지 문자열(숫자)만을 수치형(float, 실수형)으로 바꿔주는 코드

# => item_price 값을 배열 1번째부터 float 타입으로 출력

chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
chipo.groupby('item_name')['item_price'].sum()[:10]
# -

# ---
# ### [시각화로 분석 결과 살펴보기]
# > - 지금까지의 분석 결과를 간단한 시각화로 표현
# > - 아이템 별 주문의 총량을 막대 그래프로 시각화

# %matplotlib inline
import matplotlib.pyplot as plt

# +
# tolist() 함수는 시리즈를 리스트로 변환해줌
item_quantity = chipo.groupby('item_name')['quantity'].sum() 
item_name_list = item_quantity.index.tolist() # 그래프의 x 좌표값
order_cnt = item_quantity.values.tolist() # 그래프의 y 좌표값

print(len(item_quantity))
print(len(item_name_list))
# -

item_quantity

item_name_list

order_cnt

plt.figure(figsize=(10, 6))
plt.bar(item_name_list, order_cnt, align='center', color='red')
plt.ylabel('Sum Of Ordered Item')
plt.xlabel('Item Name')
plt.xticks(rotation=90)
plt.title('Distribution of Item Price')
plt.show()

# ---
# ### 1. item당 주문 총량을 막대 그래프로 표현
# ### 2. item당 주문 개수를 막대 그래프로 표현
# ### 3. item당 주문 개수(상위 10개만)를 막대 그래프로 표현
# ---

# +
plt.rc("font", family="Malgun Gothic", size=12) # 그래프에 한글 폰트 입력

orderCount = chipo.groupby('item_name')['quantity'].count()[:10]
orderSum = chipo.groupby('item_name')['quantity'].sum()[:10]

item_name_list_10 = item_quantity.index.tolist()[:10]

print(len(orderCount))
print(orderCount)
print(len(orderSum))
print(orderSum)
# -

plt.figure(figsize=(10, 6))
plt.bar(item_name_list_10, orderCount, align='center', color='orange')
plt.xticks(rotation=90)
plt.title('Item당 주문 총량')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(item_name_list_10, orderSum, align='center', color='skyblue')
plt.xticks(rotation=90)
plt.title('Item당 주문 개수')
plt.show()

# ---
# ### 4. 주문 당 계산 총액 그래프로 출력하기
# ---

# +
orderPrice = chipo.groupby('order_id')['item_price'].sum()[:10]
orderId = chipo['order_id'].unique()[:10]


print(len(orderPrice))
print(orderPrice)
print(orderId)
# -

plt.figure(figsize=(10, 6))
plt.bar(orderId, orderPrice, align='center', color='pink')
plt.ylabel('Total Price')
plt.xlabel('Order Id')
plt.title('주문당 계산총액')
plt.show()
