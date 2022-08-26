# 220412 학습데이터처리(신교수님)
import pandas as pd


df = pd.read_csv("./data/auto-mpg.csv", header=None)# header=0(default) ->첫번째 행을 열 인덱스로 쓰겠다. / header=None ->따로 0으로 시작하는 인덱스를 만들겠다.

# column명을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']

# 모든 열을 표시하기 위해서 set_option
pd.set_option('display.max_column', None)
print(df.head())

# df의 모양과 형태를 알기 위해.(크기) ->tuple 형식으로 반환(398, 9)
print(df.shape)
print(df.info())

# Dataframe의 Descrition 통계 정보
print(df.describe(include='all'))
print(df.describe(include='object')) # object만 보고싶을때 / include='number' 숫자만 보고싶을때

# 모든 열이 각각 몇 개인지 확일할때: df.count()
# count() <- dropna라는 옵션이 없음

# Dataframe에서 특정 열이 가지고 있는 고유 값이 각각 몇 개인지 확인
# NaN은 카운트하기 싫을때, dropna=True 사용
unique_value = df['origin'].value_counts()
print(unique_value)

# 평균값, 중앙값, 최대값, 최소값
# 모든 열에 대해서 각각 평균 값을 보고 싶을때.
# df.mean(), df.median(), df.max()..

# mpg 컬럼에 대한 평균값을 출력
print(df.mpg.mean())
print(df['mpg'].mean())

# mpg, weight 컬럼에 대한 평균값을 출력
print(df[['mpg', 'weight']].mean())

# 최대값/최소값(max/min())
# object type(string:문자열): ASCII(아스키코드)로 변경해서 sorting 후 max/min 결과를 반환
pd.set_option('display.max_rows', None)
print(df['horsepower'].min(), df['horsepower'].max())

# 표준편차: df.std()

# 상관계수
print(df.corr())
print(df[['mpg', 'weight']].corr())
print(df['mpg'].corr(df.displacement, method="spearman"))

# Data 전처리: horsepower의 경우, "?"가 포함되어 있어 상관계수를 구할 수가 없음.
# 1. ? ==> NaN으로 변경(replace() 메소드를 사용)
# 2. NaN의 데이터는 행단위로 삭제(dropna() 메소드를 사용)
# 3. type 자체를 float으로 변경(astype('float') 메소드를 사용)
# 4. corr() 수행
import numpy as np #(NaN)의 값으로 대체하기 위해 import
# 1. ? ==> NaN으로 변경(replace() 메소드를 사용)
df['horsepower'].replace('?', np.nan, inplace=True) # inplace=True -> 원본데이터에 수정값을 저장하겠다
# df1 = df['horsepower'].replace('?', np.nan)
# 2. NaN의 데이터는 행단위로 삭제(dropna() 메소드를 사용)
df.dropna(axis=0, inplace=True) # axis=0 -> 행단위로 삭제
# 3. type 자체를 float으로 변경(astype('float') 메소드를 사용)
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로 변환
print(df['horsepower'].dtypes)
# 4. corr() 수행
print(df.corr())