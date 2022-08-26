# 220411 기계학습프로그래밍(강교수님)
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import pandas as pd
import seaborn


def show_count_plot(feature):
    seaborn.countplot(data=df_train, x=feature,
                      hue="Survived")
    plt.show()


def show_pie_plot(feature):
    df_survive = df_train.loc[df_train["Survived"] == 1]

    # sort=False 오름차순으로 정렬하지 말고 그냥 그대로 나열하라. (.value_counts는 기본으로 정렬되어서 나옴)
    sur_info = df_survive[feature].value_counts(sort=False)
    plt.pie(sur_info, labels=sur_info.index, autopct="%0.1f%%") # autopct="%0.1f%%" -> 소숫점 첫번째자리까지 표현하고 뒤에 %붙이기
    plt.show()


def show_group_rate(feature):
    df_survive = df_train.loc[df_train["Survived"] == 1]
    df_dead = df_train.loc[df_train["Survived"] == 0]

    sur_info = df_survive[feature].value_counts(sort=False)
    dead_info = df_dead[feature].value_counts(sort=False)

    fig = plt.figure()
    plt.title("Survial Rate of " + feature)

    for i, index in enumerate(sur_info.index):
        fig.add_subplot(1, len(sur_info), i+1)
        plt.pie([sur_info[index], dead_info[index]],
                labels=["Survived", "Dead"], autopct="%0.1f%%")
        plt.title("Survival rate of {}".format(index))

    plt.show()


# def myPredict(x):
#     if x["Sex"] == "male":
#         return 0
#     else:
#         return 1



# 나의 predict 만들기
def myPredict(x):
    if x == 1 or x == 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    df_train = pd.read_csv("titanic/train.csv")
    # # print(df_train.info())
    #
    # # # Enumerate란
    # # letters = ['a', 'B', 'D', 'c']
    # # for i, l in enumerate(letters):
    # #     print(i, l)
    #
    # # 상관없어 보이는거 날림
    # # 삭제한 다음에 덮어쓰기 (앞에 df_train으로 다시 저장)
    # df_train = df_train.drop(["PassengerId", "Name", "Ticket", "Fare", "Cabin"], axis=1)
    #
    # # age의 값이 비어 있는 부분을 평균으로 채움
    # df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())
    #
    # # Embarked의 2개가 비었는데, 2개를 날리거나, 가장많은 부분으로 2개를 채워준다.
    # df_train["Embarked"] = df_train["Embarked"].fillna("S")
    #
    # # 문자 데이터를 숫자로 바꾼다.
    # df_train["Sex"] = df_train["Sex"].map({"male": 0, "female": 1})
    # df_train["Embarked"] = df_train["Embarked"].map({"Q": 0, "C": 1, "S": 2})
    #

    # RandomForestClassifier 기본 설명
    # max_depth 밑으로 가는 깊이 (for문 돌려서 어느정도는 깊이가 가장 정확한지 확인)
    # n_estimators 랜덤하게 뽑을 숫자 (몇번할꺼냐)
    # X = 학습데이터
    # Y = 정답

    # clf = RandomForestClassifier(max_depth=4, n_estimators=300)
    # Y = df_train["Survived"]
    # X = df_train.drop("Survived", axis=1)
    # clf.fit(X, Y)
    #
    # print(clf.score(X, Y)) # 몇퍼센트 맞췄는지


    # test 파일로 시험해보기
    df_test = pd.read_csv("titanic/test.csv")
    # # ID는 미리 뺴둔다 (정답 제출할때 ID가 필요함)
    # pId = df_test["PassengerId"]
    #
    # # 상관없어 보이는거 날림
    # # 삭제한 다음에 덮어쓰기 (앞에 df_train으로 다시 저장)
    # df_test = df_test.drop(["PassengerId", "Name", "Ticket", "Fare", "Cabin"], axis=1)
    #
    # # age의 값이 비어 있는 부분을 평균으로 채움
    # df_test["Age"] = df_test["Age"].fillna(df_test["Age"].mean())
    #
    # # Embarked의 2개가 비었는데, 2개를 날리거나, 가장많은 부분으로 2개를 채워준다.
    # df_test["Embarked"] = df_test["Embarked"].fillna("S")
    #
    # # 문자 데이터를 숫자로 바꾼다.
    # df_test["Sex"] = df_test["Sex"].map({"male": 0, "female": 1})
    # df_test["Embarked"] = df_test["Embarked"].map({"Q": 0, "C": 1, "S": 2})
    #
    #
    # # 분류기에 넣고 결과를 본다.
    # result = clf.predict(df_test)
    # # submit = pd.DataFrame({"PassengerID": pId, "Survived": result})
    # # # submit.csv 파일 생성
    # # submit.to_csv("titanic/submit.csv", index=False)
    #
    #
    # # 정답파일과 비교
    # gt = pd.read_csv("titanic/groundtruth.csv")
    #
    # hit = 0
    # miss = 0
    # for i in range(len(result)):
    #     if result[i] == gt.loc[i, "Survived"]:
    #         hit += 1
    #     else:
    #         miss += 1
    #
    # print(hit, miss, hit/(hit+miss))


    # 나의 predict 만들기
    # print(myPredict(df_test.loc[0]))
    # print(myPredict(df_test.loc[1]))


    # 나의 predict 정답률 보기
    pId = df_test["PassengerId"]

    myresult = []
    for i in range(len(df_test)):
        myresult.append(myPredict(df_test.loc[i, "Pclass"]))

    submit = pd.DataFrame({"PassengerID": pId, "Survived": myresult})
    # submit.csv 파일 생성
    submit.to_csv("titanic/mypredict_Pclass.csv", index=False)

    gt = pd.read_csv("titanic/groundtruth.csv")
    hit = 0
    miss = 0
    for i in range(len(myresult)):
        if myresult[i] == gt.loc[i, "Survived"]:
            hit += 1
        else:
            miss += 1

    print(hit, miss, hit/(hit+miss))