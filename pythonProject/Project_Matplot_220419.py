# 220419 학습데이터처리(신교수님)
# 한글 깨짐 현상 해결 (코드는 반드시 상단(파이썬 파일의 시작위치)에 위치해야함.)
from matplotlib import font_manager, rc
font_path = "./data/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
######################################################################

import pandas as pd

# plot 출력을 위해
import matplotlib.pyplot as plt

df = pd.read_excel('./data/남북한발전전력량.xlsx')
# print(df.head(10))
# print(df.info())

df1 = df.iloc[[0, 5], 2:]
# print(df1.head())

# row 인덱스 바꿔주기
df1.index = ['South', 'North']
# print(df1.head())

# df1.plot() # df1.plot.line() # df1.plot(kind='line') => 같은것, 아무 설정을 넣지 않으면 기본적으로 line으로 만듬
df2 = df1.T # Transpose 행과 열 자리바꿈
# df2.plot()
# df2.plot(kind='bar')
# plt.show()

# histogram
df = pd.read_csv('./data/auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']
# print(df.head())

df1 = df['mpg']
# print(df1.head())
# value_count()
# print(df1.value_count())
# df1.plot(kind='hist')

# 산점도
df.plot.scatter(x='weight', y='mpg')

# 스타일 적용
# print(plt.style.available)
plt.style.use('ggplot')

# excel 데이터를 데이터프레임 변환
df = pd.read_excel('./data/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
df.replace('-', 0, inplace=True)
# print(df.head())

# 서울에서 경기도로 이동한 데이터만 추출하여 정리해보자.
# 누락값(NaN)을 앞 데이터로 채워보자.
# method: ffill, bfill (f: Forwarding, b: Backwarding)
# forward: NaN이 나오기 바로 이전에 데이터를 사용해서 NaN값을 대체
# NaN을 서울특별시로 채워넣기: fillna(methon='ffill')
df1 = df.fillna(method='ffill')
# print(df1.head(30))

# 서울 ==> 서울로 이동한 인구는 필요없고, 다른 지역은 관심 없음 (서울에서 타지역으로 이동만 관심있음)
# 서울특별시 부분을 가져오기: mask 활용 (mask가 true인 녀석만 뽑아옴)
mask = (df1['전출지별'] == '서울특별시') & (df1['전입지별'] != '서울특별시')
# print(mask[19:19+18])
df_seoul = df1[mask]
# print(df_seoul.head())
df_seoul2 = df_seoul.drop(['전출지별'], axis=1)
df_seoul2.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df_seoul2.set_index('전입지', inplace=True)
# print(df_seoul2.head(20))

# 서울-->경기도로 이동한 인구수에 대한 선 그래프
# sr = df_seoul2.loc['경기도']
# print(sr.head())
# plt.plot(sr)
#
# plt.title("서울-->경기도 인구 이동")
# plt.xlabel("기간(연도순)")
# plt.ylabel("이동 인구수")
# plt.show()

# 서울-->대구로 이동한 인구수에 대한 선 그래프
# ss = df_seoul2.iloc[2, 11:]
# print(ss.head(20))
# plt.plot(ss)

# mask2 = (df_seoul2['전입지'] == '대구광역시')
# print(df_seoul2.loc[22])
# print(mask2)
# print(df_seoul2)
# plt.plot(mask2)

# plt.title("서울-->대구 인구 이동")
# plt.xlabel("기간(연도순)")
# plt.ylabel("이동 인구수")
# plt.show()
