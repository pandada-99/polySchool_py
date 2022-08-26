# 220426 학습데이터처리(신교수님)
# 한글 깨짐 현상 해결 (코드는 반드시 상단(파이썬 파일의 시작위치)에 위치해야함.)
import matplotlib.font_manager as fm  #매트플랏라이브러리 도움으로 폰트매니저 사용
import matplotlib

font_location = 'C:/Windows/Fonts/HMKMMAG.TTF'

font_name = fm.FontProperties(fname = font_location).get_name()

matplotlib.rc('font', family=font_name)

# from matplotlib import font_manager, rc
# font_path = "./data/malgun.ttf"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)
######################################################################

import pandas as pd

# plot 출력을 위해
import matplotlib.pyplot as plt

# 스타일 적용
# print(plt.style.available)
plt.style.use('ggplot')

df = pd.read_excel('./data/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# iloc[] <-- index (데이터를 보고, 알아서 카운팅해야 함)
# NaN을 특정 값으로 채워야 함
df = df.fillna(method="ffill")

# iloc[행, 열] / 이렇게 뽑아내는게 좋은 방법은 아님
# tmp = df.iloc[19:37, 1:]
# print(tmp.head())

# 마스트 활용하기 (서울특별시 --> 경기도)
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] == '경기도')
df_gyeonggi = df[mask]
# print(df_daegu)
df_gyeonggi.replace("-", 0, inplace=True)
df_gyeonggi = df_gyeonggi.drop(['전출지별', '전입지별'], axis=1)
# print(df_daegu)
sr_gyeonggi = df_gyeonggi.iloc[0, :]
# sr_daegu = df_daegu.loc[22, :]
# print(sr_daegu.head())
# plt.plot(sr_daegu)
# plt.show()

# 마스트 활용하기 (서울특별시 --> 대구광역시)
mask2 = (df['전출지별'] == '서울특별시') & (df['전입지별'] == '대구광역시')
df_daegu = df[mask2]
# print(df_daegu)
df_daegu.replace("-", 0, inplace=True)
df_daegu = df_daegu.drop(['전출지별', '전입지별'], axis=1)
# print(df_daegu)
sr_daegu = df_daegu.iloc[0, :]

# figsize: inch (1 inch = 2.5cn)
plt.figure(figsize=(10, 6)) # (x축의 크기, y축의 크기)
plt.xticks(rotation='vertical') # x라벨을 눕게 만들기(년도가 겹쳐보이는게 싫음)
plt.title("서울->경기 인구 이동")
plt.xlabel("기간(연도순)")
plt.ylabel("이동 인구수")

plt.plot(sr_gyeonggi, markersize=6, color='olive', marker='*')
# 범례 지정은 plot 이후에 설정할 것
plt.legend(labels=['서울 -> 경기'], loc='best')
# plt.show()

# 차트에 comment, annotation 달기
# plt.plot(sr_daegu.index, sr_daegu.values)
# y축 범위 지정 (ylim(min, max))
plt.ylim(50000, 800000)
# annotation 표시: 화살표를 그림
plt.annotate('', # 표시할 문자
             xy=(20, 620000), # 화살표의 머리 부분 (화살촉이 있는 부분)
             xytext=(2, 290000), # 화살표의 꼬리 부분 (시작점)
             xycoords='data', # 데이터 값에 따라 알아서 움직이게
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5) # lw: lane width
             )
plt.annotate('', # 표시할 문자
             xy=(47, 450000), # 화살표의 머리 부분 (화살촉이 있는 부분)
             xytext=(30, 580000), # 화살표의 꼬리 부분 (시작점)
             xycoords='data', # 데이터 값에 따라 알아서 움직이게
             arrowprops=dict(arrowstyle='->', color='green', lw=5) # lw: lane width
             )
plt.annotate('인구이동 증가(1970-1995)',
             xy=(10, 420000), # text 기준점 (대략 화살표의 중간)
             rotation=31,
             va='baseline', # vertical align
             ha='center', # hori align
             fontsize=15
             )
plt.annotate('인구이동 감소(1995-2017)',
             xy=(39, 520000), # text 기준점 (대략 화살표의 중간)
             rotation=-13,
             va='baseline', # vertical align
             ha='center', # hori align
             fontsize=15
             )
# plt.show()

# 그래프 한 화면에 여러개 만들기
fig = plt.figure(figsize=(7, 7))
# add_subplot (구성된 행, 구성된 열, 순서)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.plot(sr_daegu, marker="o", color='blue', linewidth=2)
# plot 옵션 (선 그래프에 속성의 정의)
ax2.plot(sr_gyeonggi, marker="*", color='red', linewidth=2)
# y축 범위를 지정 (각 그래프마다)
ax1.set_ylim(-1000, 20000)
ax2.set_ylim(50000, 800000)
# x축 라벨의 기울기 설정
ax1.set_xticklabels(sr_daegu.index, rotation=75)
ax2.set_xticklabels(sr_gyeonggi.index, rotation=75)
# plt.show()

# map(함수, 리스트)
# map: 리스트의 요소를 지정된 함수로 처리해주는 함수
# print(range(1970, 1980))
# print(list(range(1970, 1980))) # [1970, 1971, 1972 ..., 1979]
# var_list = []
# for var in range(1970, 1980):
#     var_list.append(str(var)) # ['1970', '1971', '1972' ..., '1979']
# print(list(map(str, range(1970, 1980)))) # ['1970', '1971', '1972' ..., '1979']

# 마스트 활용하기 (서울특별시 --> 서울특별시)
mask3 = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask3]
# print(df_seoul.head(10))
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.set_index('전입지별', inplace=True)
# print(df_seoul.head(10))
col_year = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['강원도', '충청북도', '충청남도'], col_year]
# print(df_3.head(10))
fig = plt.figure(figsize=(10, 8))
plt.title("서울->강원, 충북, 충남 인구 이동")
plt.xlabel("기간(연도순)", labelpad=25)
plt.ylabel("이동 인구수", labelpad=25)
ax = fig.add_subplot(1, 1, 1)
plt.xticks(rotation='vertical') # x라벨을 눕게 만들기(년도가 겹쳐보이는게 싫음)
ax.plot(col_year, df_3.loc['강원도', :], marker="o", color='blue', linewidth=2, label='서울 -> 강원도')
ax.plot(col_year, df_3.loc['충청북도', :], marker="o", color='pink', linewidth=2, label='서울 -> 충청북도')
ax.plot(col_year, df_3.loc['충청남도', :], marker="o", color='green', linewidth=2, label='서울 -> 충청남도')
ax.legend(loc='best')
plt.show()