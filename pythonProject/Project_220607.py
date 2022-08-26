# 220607 학습데이터처리(신교수님)
import pandas as pd
import numpy as np
import seaborn as sns # dataset load 용도

df = pd.read_csv("data/auto-mpg.csv", header=None)
# column명을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']
# 모든 열을 표시하기 위해서 set_option
pd.set_option('display.max_column', None)


# 1. 데이터 표준화
# 익숙한 단위로 사용하자
# mpg ==> kpl(km per liter)
# 1 mile: 1.690934km, 1 캘론: 3.78541리터
# mpg to kpl = 1.690934/3.78541 ==> about 0.425
mpg_to_kpl = 1.690934/3.78541
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head())

# 2. 자료형 변환 ==> 범주형 데이터 처리.
# 컬럼의 속성을 분석해서 자료형을 변환(변경)
df.info() # horsepower의 "?" dataframe 변환시 string으로 변환 ==> object
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로
print(df['horsepower'].dtype) # 해당컬럼의 타입이 뭔지 알기 위해.


# 3. 범주형 데이터 처리
# 1) numpy histogram을 이용해서 binning을 하고,
# 2) pandas cut 함수를 이용하여 범주형 데이터로 변환
# horsepower를 (low, norm, high)로 변경
count, bin_divider = np.histogram(df['horsepower'], bins=3)
print(count, bin_divider)

# 범주형 데이터 변환하기 위해 cut 메서드 사용 (bin 이름을 지정)
bin_name = ['low', 'norm', 'high'] # bin 이름은 리스트.
df['horsepower_bin'] = pd.cut(x=df['horsepower'], # 적용할 데이터 배열(리스트)
                              bins=bin_divider,
                              labels=bin_name,
                              include_lowest=True)
print(df[['horsepower', 'horsepower_bin']].head(15))

# 'low', 'norm', 'high' ==> [0, 1, 2] ==> one-hot encoding 방식 사용
# pandas 원핫인코딩: dummies 메서드 사용
hp_dummies = pd.get_dummies(df['horsepower_bin'])
print(hp_dummies.head(15))

# 4. 정규화
# 컬럼별 데이터의 범위가 차이가 많이 나면 학습에 영향을 미칠 수 있음
# 각 컬럼의 데이터들을 해당 컬럼의 최댓값으로 나누는 방법
# 정규화하기 전에는 필요에 따라 이상치 제거를 해주면 좋음
# 한번 해보세요. (col/col.max())
df.horsepower = df.horsepower/abs(df.horsepower.max())
print(df[['horsepower']].head())
# [-6, -2, 2, 1, 3, 4] ==> -1~1사이로 한 번 변경해보세요.
list = [-6, -2, 2, 1, 3, 4]
# 내가 도전한거
list_copy = []
for i in list:
    a = i/abs(min(list))
    list_copy.append(a)
print(list_copy)
# 정답
normalize_list = [data / max([abs(val) for val in list]) for data in list]
print(normalize_list)


########################################################################################################################
titanic = sns.load_dataset('titanic')
# age, fare 2개 열로 dataframe 만들기
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())

# 함수매핑 (특정 원소, 시리즈에 사용자 함수를 매핑)
# 10을 더하는 사용자 함수 정의/구현
def add_10(n):
    return n+10

# 두 객체의 합을 구하는 함수
def add_two_obj(a, b):
    return a + b

# 1) 개별 원소에 함수 매핑
# 1-1) 시리즈의 원소에 함수를 매핑: 시리즈객체.apply
sr1 = df['age'].apply(add_10)
sr_add10 = df['age'] + 10
# print(sr1.head())
# print(sr_add10.head())

# 시리즈 객체와 숫자를 이용해서 add_two_obj 사용자 함수 적용
sr2 = df['age'].apply(add_two_obj, b=10)
print(sr2.head())

# 람다도 활용 가능
sr3 = df['age'].apply(lambda x: add_10(x)) # x=df['age']

# 1-2) Dataframe에서 함수를 매핑하기 위해서는: df.applymap()
df_map = df.applymap(add_10)
print(df_map.head())

# null 여부 체크 사용자 함수
def missing_Value(series):
    return series.isnull()

result = df.apply(missing_Value, axis=0)
print(result.head(20))

# 시리즈가 입력되어서 하나의 값으로 출력하는 함수 작성
# 최대값-최소값을 반환하는 함수
def min_max(x): # x는 시리즈 (입력은 시리즈, 출력은 원소 값 하나)
    return x.max()-x.min()

# 최종적으로는 Dataframe이 입력이 되지만, 출력은 시리즈임.
result = df.apply(min_max)
print(result)
print(type(result))

print("###############################################################################################################")
# Concat, merge 실습
# 데이터는 슬라이드 5페이지
df_1 = pd.DataFrame(
    {'A': ['a0', 'a1', 'a2'],
     'B': ['b0', 'b1', 'b2'],
     'C': ['c0', 'c1', 'c2']},
        index=[0, 1, 2])
df_2 = pd.DataFrame(
    {'A': ['0a', 'a1'],
     'B': ['0b', 'b1'],
     'D': ['0d', 'd1']},
        index=[0, 1])
print(df_1)
print(df_2)

print("\nconcat 실습")
# 2개의 데이터프레임을 단순히 연결
result = pd.concat([df_1, df_2], ignore_index=True)
print(result)
# axis=0: row방향으로 연결(default), axis=1: col방향으로 연결

print("\nmerge 실습")
# merge [default: how='inner, on=None]
# on=None이라는 거는 중복되는 컬럼을 모두 merge
# on=None same as on=[A, B]
merge = pd.merge(df_1, df_2)
merge2 = pd.merge(df_1, df_2, how='outer', on='A')
merge3 = pd.merge(df_1, df_2, how='outer', on=['A', 'B'])
merge4 = pd.merge(df_1, df_2, how='inner', on='A')
merge5 = pd.merge(df_1, df_2, how='inner', on=['A', 'B'])
print(merge)
print()
print(merge2)
print()
print(merge3)
print()
print(merge4)
print()
print(merge5)

print("###############################################################################################################")
df1 = pd.read_excel('data/stock price.xlsx')
df2 = pd.read_excel('data/stock valuation.xlsx')

# on=None, on='id'
# 중복되는 것만 추출
# default: inner, on=None
merge_inner = pd.merge(df1, df2)
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print()
print(merge_inner)
print()
print(merge_outer)

# Left Join 하나만.
# DB: select = from dif left outer join df2 on df1.stock_name = df2.name
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print()
print(merge_left)