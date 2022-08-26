# 220524 학습데이터처리(신교수님)
import pandas as pd
import seaborn as sns # seaborn 내에 타이타닉, 펭귄 데이터셋을 로드하기 위해서

pd.set_option('display.max_columns', None) # 실행시 컬럼 전체가 표현되도록

# 타이타닉 데이터셋 로드
df_titanic = sns.load_dataset('titanic')

# NaN을 확인하는 방법 중에 한개. info()
print(df_titanic.info())
# deck 열이 NaN이 많이 있는 것을 확인
# value_counts() ==> NaN이 몇 개인지 파악
# dropna=False => NaN값도 세어준다 (dropna="", dropna=0 (bool: False 의미))
print(df_titanic['deck'].value_counts(dropna=False))

# NaN을 확인하는 방법 중에 한개. isnull()
print(df_titanic.head().isnull())
# isnull().all, isnull().any
# all: 각각의 열의 데이터가 모두 null인지를 확인해서 True, False 반환
# any: 열의 데이터 중에 하나라도 null인지를 확인
print(df_titanic.head().isnull().all())
print(df_titanic.head(50).isnull().any())
# 데이터프레임에서 하나라도 null이 있으면 True 반환하고 싶을 경우
print(df_titanic.isnull().any())
print("=========================================================================================================")
# 각 열에서 NaN인 데이터의 개수를 반환
# sum() ==> 대신에 count도 사용 가능
# sum(axis 옵션), isnull
# axis=0: column, axis=1: row를 의미
# 해당모듈, 특정한 모듈이 컬럼단위로 계산하는 모듈이면 axis=0: col
print(df_titanic.isnull().sum()) # df_titanic.isnull().sum(axis=0)
# count: 열의 개수를 카운팅하는데.. 옵션에 dropna와 같은 내용이 없음
# count() 자체는 NaN를 배제하고 카운팅
# isnull.sum() <-- 모른다고 하더라도 시리즈 연산을 하면 각 열의 NaN 개수 확인가능
# 시리즈 연산: 숫자 (+, -, *) 시리즈, 시리즈 + 10
print(len(df_titanic) - (df_titanic.count())) # 열의 개수(len()) - count()

# NaN을 확인하는 방법은 여러가지가 있는걸 확인
# 내가 학습시킨다고하면, Deck 열은 사용하는게 좋을까?
# Deck 열은 NaN 대략 600개 정도 되기 때문에 80%정도가 NaN
# 유츄하는데 오히려 성능에 악영향을 미칠 수 있으므로 해당 컬럼을 삭제
df_drop = df_titanic.drop(columns=['deck'])
# NaN이 아닌 값이 최소 몇 개 이상 나와야 된다는 것(그보다 적게 나오면 drop)
df_thresh = df_titanic.dropna(axis=1, thresh=500)
print(df_drop.head(), '\n', df_thresh.head())
# age 열에 NaN가 있는 행을 삭제
df_age = df_titanic.dropna(subset=['age'], axis=0, how='any') # how='all'인거랑 같음(subset이 하나라서)
df_age_deck = df_titanic.dropna(subset=['age', 'deck'], axis=0, how='all') # 'age', 'deck'이 둘다 NaN여야 삭제
print(df_age, len(df_age))

# age 열에 NaN일 경우에는, mean값을 채워넣자.
# mean(axis옵션), 0: col, 1: row
# 값을 채워넣을때, 경우에 따라 학습모델에 의해 추정된 값을 사용하기도 한다.
mean_age = df_titanic['age'].mean()
# fillna 메서드: NaN replace 어떤값
df_fillna = df_titanic['age'].fillna(mean_age)
print(df_titanic.head(15), df_fillna.head(15))

# ffill, bfill (Forwarding, Backwarding)
df_ffill = df_titanic['embark_town'].fillna(method='ffill')


# ======================================================================================================================
df_pg = sns.load_dataset("penguins")
print(df_pg.info())


# 1) 결측치 데이터 (NaN) 처리
# 성별은 11개의 데이터가 NaN으로 확인되었고, 성별은 유추에서 정하기가 어려움
# 결측지가 있는 데이터 추출?
print(df_pg.isnull().sum())
# mask를 생성 (결측치가 하나라도 있는 행에 대해서 True, False)
print(df_pg.isnull().any(axis=1))
print(df_pg[df_pg.isnull().any(axis=1)])
# 3, 339번 인덱스와 성별 컬럼은 drop
df_pg = df_pg.drop(columns='sex')
df_pg = df_pg.dropna(axis=0)
print(df_pg.info())


# 2) 중복 데이터 처리
# 중복데이터를 확인: duplicated()
# 기본적으로는 중복데이터 삭제
print(df_pg.duplicated()) # 중복데이터 없음
# 중량이 제일 많이 나가는 데이터와 동일한 데이터를 추가해보자
print(df_pg['body_mass_g'].max(), '\n', df_pg.tail(2))
print(df_pg[df_pg['body_mass_g'] == df_pg['body_mass_g'].max()])
"""
     species   island       bill_length_mm    bill_depth_mm    flipper_length_mm      body_mass_g
237   Gentoo   Biscoe            49.2              15.2              221.0               6300.0  
"""
df_pg.loc[344] = ['Gentoo', 'Biscoe', 49.2, 15.2, 221.0, 6300.0]
print(df_pg.duplicated())
# df_pg = df_pg.drop(index=344)
# print(df_pg.duplicated())
df_pg.drop_duplicates(inplace=True)
print(df_pg)

df_num = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                       'c2': [1, 1, 1, 2, 2],
                       'c3': [1, 1, 2, 2, 2]})
print(df_num)
print(df_num.duplicated())
print(df_num['c2'].duplicated())


# 3) 이상치 데이터 처리
# z-score를 사용
# z-score 함수작성: (데이터-평균)/표준편차
# np.mean()<--평균, np.std()<-- 표준편차

import numpy as np
# z-score가 -2이하, 2이상되는 데이터(Data frame)을 반환하는 함수
# (x-u)/std
# outlier(df_pg, 'body_mess_g', 2)
def outlier(df, col, z_threshold):
    # df[col]: x / df['body_mess_g']
    return df[abs((df[col]-np.mean(df[col])))/np.std(df[col]) > z_threshold].index
def inlier(df, col, z_threshold):
    # df[col]: x / df['body_mess_g']
    return df[abs((df[col]-np.mean(df[col])))/np.std(df[col]) <= z_threshold].index

print(df_pg.loc[outlier(df_pg, 'body_mass_g', 2)])
print(df_pg.loc[inlier(df_pg, 'body_mass_g', 2)])