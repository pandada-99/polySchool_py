# https://www.youtube.com/watch?v=aqp_9HV58Ls&t=135&ab_channel=MinsukHeo%ED%97%88%EB%AF%BC%EC%84%9D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# **********데이터 가져와서 읽기**********
import pandas as pd
train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')

# 모든 열을 보고싶을때.
pd.set_option('display.max_columns', None)
# print(train.head())
# print(test.head()) # Survived 열 없음
# Survived: 0 = No, 1 = Yes

# 모든 행을 보고싶을때.
pd.set_option('display.max_rows', None)

# 데이터 정보 보기
# print(train.info())
# print(test.info())

# 데이터에서 null인 항목 확인하기
# print(train.isnull().sum())
# print(test.isnull().sum())

# **********시각화하기**********
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 반복해서 불러올 내용을 함수로 정리
def bar_chart (feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.show()

# 특징(성별, 객실 등)에 따라 생존과 죽은 인원 비교
# bar_chart('Sex')
# bar_chart('Pclass')
# bar_chart('SibSp')
# bar_chart('Parch')
# bar_chart('Embarked')


# **********데이터 전처리**********

# train과 test를 한번에 묶기
train_test_data = [train, test]
# print(train_test_data[0])
# print(train_test_data[1])


# *****Name*****
# 특징이 나오는 부분 추출('Title' column 생성)
for dataset in train_test_data:
    dataset['Title'] = dataset['Name'].str.extract('([A-Za-z]+)\.', expand=False)

# 비슷한 것끼리 묶기
title_mapping = {"Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3, "Dr": 3, "Rev": 3, "Col": 3, "Major": 3, "Mlle": 3,
                 "Countess": 3, "Ms": 3, "Lady": 3, "Jonkheer": 3, "Don": 3, "Dona": 3, "Mme": 3, "Cept": 3, "Sir": 3}
for dataset in train_test_data:
    dataset['Title'] = dataset['Title'].map(title_mapping)

# bar_chart('Title')

# 이제 'Name'은 필요가 없어 삭제
train.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)


# *****Sex*****
# 남자는 0, 여자는 1로 변경
sex_mapping = {"male": 0, "female": 1}
for dataset in train_test_data:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)


# *****Age*****
# 없는 나이 채우기
# 어떤값으로? Miss는 Miss의 평균나이로, Mr는 Mr의 평균나이로 채우기 (아까 추출한 Title 활용)
train["Age"].fillna(train.groupby("Title")["Age"].transform("median"), inplace=True)
test["Age"].fillna(test.groupby("Title")["Age"].transform("median"), inplace=True)

# null부분이 채워졌는지 확인
# print(train.isnull().sum())

# 나이를 카테고리별로 묶어버리기(Binning)
# child: 0, young: 1, adult: 2, mid-age: 3, senior: 4
# print(len(train_test_data))
for dataset in train_test_data:
    dataset.loc[ dataset['Age'] <= 16, 'Age'] = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 26), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 26) & (dataset['Age'] <= 36), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 36) & (dataset['Age'] <= 62), 'Age'] = 3
    dataset.loc[ dataset['Age'] > 62, 'Age'] = 4

# print(train_test_data[0].loc[:,'Age'])


# *****Embarked*****
# 어디서 탄 사람들이 어떤 등급의 호실을 사용했는지 확인
Pclass1 = train[train['Pclass']==1]['Embarked'].value_counts()
Pclass2 = train[train['Pclass']==2]['Embarked'].value_counts()
Pclass3 = train[train['Pclass']==3]['Embarked'].value_counts()
df = pd.DataFrame([Pclass1, Pclass2, Pclass3])
df.index = ['1st class', '2nd class', '3rd class']
df.plot(kind='bar', stacked=True, figsize=(10, 5))
# plt.show()

# 빈부분에 가장 많은 S를 집어넣어라
for dataset in train_test_data:
    dataset['Embarked'] = dataset['Embarked'].fillna('S')

# "S": 0, "C": 1, "Q": 2로 맵핑
embarked_mapping = {"S": 0, "C": 1, "Q": 2}
for dataset in train_test_data:
    dataset['Embarked'] = dataset['Embarked'].map(embarked_mapping)


# *****Fare*****
# 없는 값은 같은 class의 중간값으로 채운다
train["Fare"].fillna(train.groupby("Pclass")["Fare"].transform("median"), inplace=True)
test["Fare"].fillna(test.groupby("Pclass")["Fare"].transform("median"), inplace=True)

# 티켓가격을 카테고리별로 묶어버리기(Binning)
for dataset in train_test_data:
    dataset.loc[ dataset['Fare'] <= 17, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 17) & (dataset['Fare'] <= 30), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 30) & (dataset['Fare'] <= 100), 'Fare'] = 2
    dataset.loc[ dataset['Fare'] > 100, 'Fare'] = 3


# *****Cabin*****
# print(train.Cabin.value_counts())
# Cabin값 맨앞의 'chr'만 뽑아냄
for dataset in train_test_data:
    dataset['Cabin'] = dataset['Cabin'].str[:1]

# 어떤 객실이 어떤 Class에 사용되었는지 확인
# A,B,C,D,E 객실은 '1st class'에만 사용 되었다.
Pclass1 = train[train['Pclass'] == 1]['Cabin'].value_counts()
Pclass2 = train[train['Pclass'] == 2]['Cabin'].value_counts()
Pclass3 = train[train['Pclass'] == 3]['Cabin'].value_counts()
df = pd.DataFrame([Pclass1, Pclass2, Pclass3])
df.index = ['1st class', '2nd class', '3rd class']
df.plot(kind='bar', stacked=True, figsize=(10, 5))
# plt.show()

# 맵핑
# 소수로 하는 이유: 차이가 커지면 더 중요하게 받아들이기 때문에 범위의 차이를 낮춘다.
# 예를 들어 남여는 중요한데 차이가 1이고, 티켓의 가격은 중요하지 않은데 차이가 2~3이면 티켓의 가격을 남여의 차이보다 훨씬 중요하게 다룬다.
cabin_mapping = {"A": 0, "B": 0.4, "C": 0.8, "D": 1.2, "E": 1.6, "F": 2, "G": 2.4, "T": 2.8}
for dataset in train_test_data:
    dataset['Cabin'] = dataset['Cabin'].map(cabin_mapping)

# 없는 값은 같은 class의 중간값으로 채운다
train["Cabin"].fillna(train.groupby("Pclass")["Cabin"].transform("median"), inplace=True)
test["Cabin"].fillna(test.groupby("Pclass")["Cabin"].transform("median"), inplace=True)


# *****FamilySize*****
# 'SibSp'과 'Parch'수를 합쳐 FamilySize로 만든다. (+1은 자기자신)
train["FamilySize"] = train["SibSp"] + train["Parch"] + 1
test["FamilySize"] = test["SibSp"] + test["Parch"] + 1

# 맵핑
family_mapping = {1: 0, 2: 0.4, 3: 0.8, 4: 1.2, 5: 1.6, 6: 2, 7: 2.4, 8: 2.8, 9: 3.2, 10: 3.6, 11: 4}
for dataset in train_test_data:
    dataset['FamilySize'] = dataset['FamilySize'].map(family_mapping)


# 필요없는 부분 삭제
features_drop = ['Ticket', 'SibSp', 'Parch']
train = train.drop(features_drop, axis=1)
test = test.drop(features_drop, axis=1)
train = train.drop('PassengerId', axis=1)

# print(train.head())
# print(test.head())


# **********Modelling**********

# *****K-folde*****
K_fold = KFold(n_splits=10, shuffle=True, random_state=0)


# *****kNN*****
# clf = KNeighborsClassifier(n_neighbors=13)
# scoring = 'accuracy'
# score = cross_val_score(clf, train, target, cv=k_fold, n_jobs=1, scoring=scoring)
# print(score)


# *****Decision Tree*****
# clf = DecisionTreeClassifier()
# scoring = 'accuracy'
# score = cross_val_score(clf, train, target, cv=k_fold, n_jobs=1, scoring=scoring)
# print(score)


# *****교수님 강의 참고*****

# for i in range(1, 20):
#     clf = RandomForestClassifier(max_depth=i, n_estimators=300)
#     x = train.drop("Survived", axis=1)
#     y = train["Survived"]
#     clf.fit(x, y)
#     print('max_depth이', i, '일 때', clf.score(x, y))

clf = RandomForestClassifier(max_depth=3, n_estimators=300)
x = train.drop("Survived", axis=1)
y = train["Survived"]
clf.fit(x, y)

# test 파일로 시험해보기
test_PID = test["PassengerId"]
test = test.drop(["PassengerId"], axis=1)

result = clf.predict(test)
# print(result)
submit = pd.DataFrame({"PassengerID": test_PID, "Survived": result})
submit.to_csv("titanic/myprdict_first.csv", index=False)


# 정답파일과 비교
gt = pd.read_csv("titanic/groundtruth.csv")

hit = 0
miss = 0
for i in range(len(result)):
    if result[i] == gt.loc[i, "Survived"]:
        hit += 1
    else:
        miss += 1
print(hit, miss, hit/(hit+miss))