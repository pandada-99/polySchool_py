# 220621 학습데이터처리(신교수님)
import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 모든 행과 5개의 열을 가지고 와서 dataframe 생성
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(f'* 승객수: {len(df)}')
# print(df.head())
print()

# Groupby 실습 (SQL, DB 시간에 다룬 내용)
# class 열을 기반으로 group 객체 생성
grouped = df.groupby(['class'])
# print(grouped.head())
# print(grouped.sum())

# 그룹 전체를 iteration을 돌면서 출력
# 그룹 객체(grouped): key [first, second, third]
for key, group in grouped:
    print("* key:", key)
    print("* number:", len(group))
    # print(group.head())
    print()

# 연산 메서드 적용
# 연산 메서드 사용시에는 연산이 가능한 열에 대해서만 선택적으로 연산을 수행
# 문자열을 포함한 sex, class 열을 제외하고
# 숫자형 데이터에 대해서만 평균을 구해보자
average = grouped.mean()
# print(average)
# 결과: 1등석의 경우, 평균 나이가 제일 많고, 구조확률이 약 62%로 제일 높음

# 개별 그룹 선택 (first or second class 선택 등등)
group3 = grouped.get_group('Third')
# print(group3.head())

grouped_two = df.groupby(['class', 'sex'])

for key, group in grouped_two:
    print("* key:", key)
    print("* number:", len(group))
    # print(group.head())
    print()

# grouped_two라는 객체에 대해서 연산 메서드 적용
average = grouped_two.mean()
# print(average)
"""
결과 분석 내용 작성
: 여자가 남자보다 생존 확률이 높다,
여자가 남자보다 평균나이가 어리다,
일등석은 평균나이게 가장 많다.
"""

# 개별 그룹 선택 (first or second class 선택 등등)
# 멀티인덱스 형태로 되어있는 그룹에서 개별 그룹을 가지고 오고 싶을때
# 튜플형태로 컬럼을 지정하면 됨 (First group, Second group, Third group..)
# (3등석에 여성의 테이터를 가지고 오고 싶을때): ('Third', 'female')
group3f = grouped_two.get_group( ('Third', 'female') )
# print(group3f.head())

# Filtering
# 예: 나이 평균이 30보다 작은 그룹만을 필터링해서 DF로 반환
average = grouped.mean()
print(average)
# 평균 나이가 30 미만인 그룹(클래스)은 second, third 그룹
age_filter = grouped.filter(lambda x: x.age.mean() < 30)