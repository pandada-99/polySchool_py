# 220503 학습데이터처리(신교수님)
from matplotlib import font_manager, rc
font_path = "./data/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
########################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel("data/남북한발전전력량.xlsx", header=0)

# 북한의 전력 발전량만 가지고 옴
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis=1, inplace=True)
# df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T

# 증감율 계산 (전년대비 증감율 컬럼을 만들고, 이 컬럼을 그래프로 그려주기 위해)
df['총발전량-1년'] = df['합계'].shift(1) # (-1)
# print(df.head())
df['증감율'] = (df['합계']/df['총발전량-1년']-1)*100
# df['증감율'] = ((df['합계']-df['총발전량-1년'])/df['총발전량-1년'])*100

# shift 사용하지 않고 증감율 계산하기


# 막대그래프 stack, 선 그래프를 겹쳐서 그리기.
ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(12, 7), stacked=True)

# ax2: 선 그래프
ax2 = ax1.twinx() # x-axis는 공유하고, y-axis는 따로 표현하고자 할때.
ax2.plot(df.index, df.증감율, ls='--', marker='o', color='green')

# 그래프 꾸미기
plt.title("북한 전력 발전량(1990 ~ 2016)", fontsize=30)
ax1.set_xlabel("연도", fontsize=15)
ax1.set_ylabel("발전량(억 KWh)", fontsize=15)
ax2.set_ylabel("전년 대비 증감율(%)", fontsize=15)
ax1.legend(loc='upper left')

ax1.set_ylim([0, 500])
ax2.set_ylim([-50, 50])

plt.show()


# ======================================================================================================================
# pie 차트(파이 차트) 만들기
# header=0(default) ->첫번째 행을 열 인덱스로 쓰겠다. / header=None ->따로 0으로 시작하는 인덱스를 만들겠다.
df = pd.read_csv("data/auto-mpg.csv", header=None)

# column명을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']

# # groupby()로 만들기
# # Groupby 사용을 위해서 count된 값을 넣기 위한 count 컬럼 생성
# df['count'] = 1
#
# # 제조국가(origin)열을 기준으로 그룹화 및 합계 계산
# df_origin = df.groupby('origin').sum()
# print(df_origin.head())
#
# # 제조국가 값(1, 2, 3)을 usa, eu, japan으로 변경
# df_origin.index = ['USA', 'EU', 'JAPAN']
# df_origin['count'].plot(kind='pie', figsize=(7, 5), autopct='%.2f%%', colors=['chocolate', 'bisque', 'cadetblue'])
# plt.title('Model Origin')
# plt.legend(labels=df_origin.index, loc='upper right')
#
# plt.show()

# value_counts()로 만들기
df_origin = df['origin'].value_counts()
df_origin = df_origin.sort_index()
# print(df_origin.head())

# 제조국가 값(1, 2, 3)을 usa, eu, japan으로 변경
df_origin.index = ['USA', 'EU', 'JAPAN']
df_origin.plot(kind='pie', figsize=(7, 5), autopct='%.2f%%', colors=['chocolate', 'bisque', 'cadetblue'])
plt.title('Model Origin')
plt.legend(labels=df_origin.index, loc='upper right')

plt.show()


# ======================================================================================================================
import seaborn as sns

# Seaborn: Regression(선형회귀) 포함된 산점도 그래프
df_scatter = df[['weight', 'mpg']]
# print(df_scatter.head())

# 산점도에서 선형회귀 선을 같이 그리는 함수(라이브러리)
sns.regplot(x='weight', y='mpg', data=df_scatter, scatter_kws={'color':'green'}, line_kws={'color':'red'})
plt.show()


# ======================================================================================================================
# 참고: "RANSAC" 랜덤으로 두 점을 정해서, 두 점을 잇는 직선을 그려 다른 점들간의 거리를 구함. 가장 거리가 작은 직선 => 이 점들과 관련이 있는 직선

# 산점도: weight, mpg
x = list(df['weight'])
y = list(df['mpg'])

# 선형 회귀 (1차: 직선, numpy: polyfit 사용)
# 직선의 방정식에서 출력되는 것 y = ax + b (기울기: a와, 절편: b)
grad, intercept = np.polyfit(x, y, deg=1)
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y, color="green")

# linspace(start, end, num)
# num: start, end를 몇 등분할 것인지.
# start:1, end:10, num:10 10등분을 하는거니까 x축이 1씩 증가
# start:1, end:10, num:20 20등분을 하는거니까 x축이 0.5씩 증가
xseq = np.linspace(min(x), max(x), num=len(x))
# 직선을 그리기 위해 x축은 linspace를 통해서 지정
# y축은 grad, intercept를 구했죠. y = grad * x + intercept
ax.plot(xseq, grad+xseq+intercept, color="red", lw=2.5)
plt.show()


# ======================================================================================================================
# Seaborn: 히트맵 그래프
# Dataset: Seaborn에서 제공하는 flights라는 데이터셋 사용
# 연도/월별 탑승자수를 한 눈에 보기 위해 히트맵 작성
flight_data = sns.load_dataset("flights")
# pivot() 메소드 사용
df = flight_data.pivot('month', 'year', 'passengers')
# print(df.head())

ax = sns.heatmap(df, annot=True, fmt='d')
plt.title("Heatmap of Flight by Seaborn")
plt.show()