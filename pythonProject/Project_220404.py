from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import pandas as pd
import seaborn

# main함수 밖에 define할것
def showCountPlot (feature):
    seaborn.countplot(data=df_train, x=feature, hue="Survived")
    plt.show()

def showPiePlot(feature):
    # 생존 그룹과 그렇지 않은 그룹으로 나눈다.
    df_survive = df_train.loc[df_train["Survived"] == "Alive"]
    df_dead = df_train.loc[df_train["Survived"] == "Dead"]

    # feature 열의 생존자와 사망자 수를 카운트 한다.
    sur_info = df_survive[feature].value_counts(sort=False)

    # 전체 생존자 수 대비 category 별 생존 비율
    category = sur_info.index
    plt.title("Survival Rate in Total ({0})".format(feature))
    plt.pie(sur_info, labels=category, autopct="%0.1f%%")
    plt.show()

# 과제 (성별에 따른 생존 비율)
def showSexPiePlot():
    df_male = df_train.loc[df_train["Sex"] == "male"]
    df_female = df_train.loc[df_train["Sex"] == "female"]

    male_sur_info = df_male["Survived"].value_counts(sort=False)
    female_sur_info = df_female["Survived"].value_counts(sort=False)

    category = male_sur_info.index
    plt.title("Survival Rate in Total Survived male")
    plt.pie(male_sur_info, labels=category, autopct="%0.1f%%")
    plt.show()

    category = female_sur_info.index
    plt.title("Survival Rate in Total Survived female")
    plt.pie(female_sur_info, labels=category, autopct="%0.1f%%")
    plt.show()

# 과제 (좌석등급에 따른 생존 비율)
def showPclassPiePlot():
    df_1st = df_train.loc[df_train["Pclass"] == "1st"]
    df_Business = df_train.loc[df_train["Pclass"] == "Business"]
    df_Economy = df_train.loc[df_train["Pclass"] == "Economy"]

    sur_info_1st = df_1st["Survived"].value_counts(sort=False)
    sur_info_2st = df_Business["Survived"].value_counts(sort=False)
    sur_info_3st = df_Economy["Survived"].value_counts(sort=False)

    category = sur_info_1st.index
    plt.title("Survival Rate in Total Survived 1st")
    plt.pie(sur_info_1st, labels=category, autopct="%0.1f%%")
    plt.show()

    category = sur_info_2st.index
    plt.title("Survival Rate in Total Survived Business")
    plt.pie(sur_info_2st, labels=category, autopct="%0.1f%%")
    plt.show()

    category = sur_info_3st.index
    plt.title("Survival Rate in Total Survived Economy")
    plt.pie(sur_info_3st, labels=category, autopct="%0.1f%%")
    plt.show()

# main 함수
if __name__== '__main__':
    df_train = pd.read_csv("titanic/train.csv")

    # 히스토그램에서 보기 좋게 라벨링
    df_train["Pclass"] = df_train["Pclass"]\
        .replace(1, "1st")\
        .replace(2, "Business")\
        .replace(3, "Economy")

    df_train["Survived"] = df_train["Survived"]\
        .replace(1, "Alive")\
        .replace(0, "Dead")

    # 좌석 등급에 대한 히스토그램
    # seaborn.set_style(style="darkgrid")
    # showCountPlot("Pclass")
    # showCountPlot("Sex")
    # showCountPlot("Age")
    # showCountPlot("SibSp")
    # showCountPlot("Parch")
    # showCountPlot("Fare")
    # showCountPlot("Embarked")

    # Pie plot
    # showPiePlot("Pclass")
    # showPiePlot("Sex")
    # showPiePlot("Age")
    # showPiePlot("SibSp")
    # showPiePlot("Parch")
    # showPiePlot("Fare")
    # showPiePlot("Embarked")

    # 과제 (성별에 따른 생존 비율)
    showSexPiePlot()


    # 과제 (좌석등급에 따른 생존 비율)
    showPclassPiePlot()