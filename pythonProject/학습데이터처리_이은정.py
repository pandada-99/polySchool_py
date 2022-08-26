import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 모든 열을 표시하기 위해서 set_option
pd.set_option('display.max_column', None)

########################################################################################################################
# header=0(default) ->첫번째 행을 열 인덱스로 쓰겠다. / header=None ->따로 0으로 시작하는 인덱스를 만들겠다.
df = pd.read_csv("./data/Pokemon.csv", header=0)

# df의 모양과 형태를 알기 위해.
# print(df.head())
# print(df.shape)
# print(df.info())

# 1. Attack컬럼의 값을 기준으로 내림차순정렬 했을대 상위 400위까지 포켓몬들과 401~800위까지의 포켓몬들에서 전설포켓몬(Legendary칼럼)의 숫자 차이를 구하시오.
df_sorted_up = df.sort_values(by=['Attack', '#'], ascending=[False, True]).iloc[:400]
# print(df_sorted_up.shape)
# print(df_sorted_up.head())
# print(df_sorted_up.tail())
df_sorted_down = df.sort_values(by=['Attack', '#'], ascending=[False, True]).iloc[400:]
# print(df_sorted_down.shape)
# print(df_sorted_down.head())
# print(df_sorted_down.tail())

# print(len(df_sorted_up.loc[df['Legendary'] == True]))
# print(len(df_sorted_down.loc[df['Legendary'] == True]))

# 2. Type 1 컬럼의 속성이 Fire인 포켓몬들의 Attack의 평균이상인 Water속성의 포켓몬 수를 구하시오.
df_fire = df.loc[df['Type 1'] == 'Fire']
# print(df_fire.shape)
# print(df_fire.describe()) # mean = 85
df_water = df.loc[df['Type 1'] == 'Water']
df_water_attack = df_water.loc[df['Attack'] >= 85]
# print(len(df_water_attack))
# print(df_water_attack.shape)

########################################################################################################################
# header=0(default) ->첫번째 행을 열 인덱스로 쓰겠다. / header=None ->따로 0으로 시작하는 인덱스를 만들겠다.
df = pd.read_csv("./data/bank.csv", header=0, delimiter=';')

# df의 모양과 형태를 알기 위해.
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

# 3. 마케팅 응답 고객들의 나이를 10살 단위로 변환 했을 때, 가장 많은 인원을 가진 "나이대와 인원수"를 도출하시오.
bins = list(range(0, 91, 10)) # age min = 19 / max = 87
bins_df = [str(x)+"이상 "+str(x+10)+"미만" for x in bins]
# df['age_bins'] = pd.cut(df['age'], bins, right=False, labels=bins_df[:-1])
# print(df['age_bins'].value_counts())

# 4. 나이가 25살 이상 29살 미만인 응답 고객들중 housing 컬럼의 값이 yes인 고객의 수는 몇 명인가?
df_25to29 = df.loc[(df['age'] >= 25) & (df['age'] < 29)]
df_house = df_25to29.loc[df['housing'] == 'yes']
# print(df_house.shape)

# 5. numeric한 값을 가지지 않은 컬럼들중 unique한 값을 가장 많이 가지는 컬럼의 이름과 unique한 값의 개수는 몇 개인지 구하시오.
# print(df.info())
# print(df['job'].nunique())
# print(df['marital'].nunique())
# print(df['education'].nunique())
# print(df['default'].nunique())
# print(df['housing'].nunique())
# print(df['loan'].nunique())
# print(df['contact'].nunique())
# print(df['month'].nunique())
# print(df['poutcome'].nunique())
# print(df['y'].nunique())

# 6. balance컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을때 상위 100개 데이터의 balance값의 평균은 얼마인가?
# print(df.describe()) # balance mean => 1422.657819
df_balance = df.loc[df['balance'] >= df['balance'].mean()]
df_balance = df_balance.sort_index(ascending=False).iloc[:100]
# print(df_balance['balance'].mean())

# 7. 가장 많이 마케팅(전화)을 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자),달(영문)으로 표기)
df_contact = df.loc[df['contact'] != 'unknown']
# print(df_contact)
# print(df_contact['month'].value_counts()) # month max => jul
# df_jul = df_contact.loc[df['month'] == 'jul']
# print(df_jul['day'].value_counts())
#=================> 하면 31, jul가 나오지만 이게 최대 갯수 날짜 인지는 모름(ex.8월 12일에 열라 많을 수 있으니까)

# 7월 31일이 53개니까 53보다 많은 달은 다 조사해봐야함
# print(df_contact['month'].value_counts()) # aug, may, nov, apr, feb, jan, jun, oct)

# df_may = df_contact.loc[df['month'] == 'aug']
# print(df_may['day'].value_counts()) # 19일 44
#
# df_may = df_contact.loc[df['month'] == 'may']
# print(df_may['day'].value_counts()) # 18일 62
#
# df_may = df_contact.loc[df['month'] == 'nov']
# print(df_may['day'].value_counts()) # 19일 84
#
# df_may = df_contact.loc[df['month'] == 'apr']
# print(df_may['day'].value_counts()) # 17일 60
#
# df_may = df_contact.loc[df['month'] == 'feb']
# print(df_may['day'].value_counts()) # 2일 42
#
# df_may = df_contact.loc[df['month'] == 'jan']
# print(df_may['day'].value_counts()) # 29일 57
#
# df_may = df_contact.loc[df['month'] == 'jun']
# print(df_may['day'].value_counts()) # 1일 13
#
# df_may = df_contact.loc[df['month'] == 'oct']
# print(df_may['day'].value_counts()) # 27일 9

# 8~9. age와 balance컬럼 간의 상관계수를 구하고, hitmap 그래프로 표현하시오.
# print(df.corr())
df_age_balance = df[['age', 'balance']]
# print(df_age_balance.corr())

# plt.figure(figsize=(10, 10))
# sns.heatmap(data=df_age_balance.corr(), annot=True, fmt='.3f', linewidths=.5, cmap='Blues')
# plt.show()

########################################################################################################################
# header=0(default) ->첫번째 행을 열 인덱스로 쓰겠다. / header=None ->따로 0으로 시작하는 인덱스를 만들겠다.
df = pd.read_csv("./data/healthcare-dataset-stroke-data.csv", header=0)

# df의 모양과 형태를 알기 위해.
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

# 10. 성별이 Male인 환자들의 age의 평균값(소수점 3자리까지, 반올림)을 구하시오.
df_male = df[df['gender'] == 'Male']
mage = df_male['age'].mean()
# print(round(mage, 3))

# 11. bmi컬럼의 결측치를 bmi컬럼의 결측치를 제외한 나머지 값들의 평균값으로 채웠을 경우 bmi컬럼의 평균을 소숫점 이하 3자리(반올림)까지 구하시오.
df_bmi = df['bmi'].fillna(df['bmi'].mean())
# print(round(df_bmi.mean(), 3))

# 12. bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi값으로 대채한 후 대체된 bmi컬럼의 평균을 소숫점 이하 3자리(반올림)까지 구하시오.
bins = list(range(0, 91, 10)) # age min = 19 / max = 87
bins_df = [str(x)+"대" for x in bins]
df['age_bins'] = pd.cut(df['age'], bins, right=False, labels=bins_df[:-1])
# print(df['age_bins'].value_counts())

df['bmi'].fillna(df.groupby('age_bins')['bmi'].transform("mean"), inplace=True)
df_mean = df.groupby(['age_bins'], as_index=False).mean()
# print(df_mean['bmi'])
# print(df['bmi'].head())

# print(df.info())
# print(round(df['bmi'].mean(), 3))