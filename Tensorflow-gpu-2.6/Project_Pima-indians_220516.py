import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    df = pd.read_csv("./pima-indians_data/diabetes.csv")

    # # 임신 횟수에 따른 당뇨 확률
    # df_diabetes = df.loc[df["Outcome"] == 1] # 당뇨인 사람
    # df_normal = df.loc[df["Outcome"] == 0] # 당뇨가 아닌 사람
    #
    # hist1 = df_diabetes.value_counts("Pregnancies").sort_index()
    # hist2 = df_normal.value_counts("Pregnancies").sort_index()
    # # sort_index(): index 기준으로 정렬, sort_values: 값 기준으로 오름차순 정렬
    # hist3 = hist1 / (hist1 + hist2)
    #
    # print(hist3.fillna(1))
    ####################################################################################################################

    # # 칼럼들의 상관 관계 (히트맵 시각화)
    # plt.figure(figsize=(10, 10))
    # seaborn.heatmap(df.corr(), annot=True, cmap=plt.cm.Pastel1, linewidths=0.1, linecolor='white')
    # plt.show()
    ####################################################################################################################

    # # Glucose(공복 혈당 농도)와 당뇨와의 관계 시각화
    # grid = seaborn.FacetGrid(df, col="Outcome") # Outcome별로 그래프를 그림
    # grid.map(plt.hist, "Glucose", bins=10) # Glucose의 히스토그램을 그림 (구간을 10개로 나눔)
    # plt.show()
    ####################################################################################################################

    # 신경망 학습
    dataset = np.loadtxt("./pima-indians_data/diabetes.csv", delimiter=",")
    # print(dataset)

    # test 하기 위해 학습 돌릴 데이터 분리
    X = dataset[0:700, 0:8]
    Y = dataset[0:700, 8]
    testX = dataset[700:, 0:8]
    testY = dataset[700:, 8]

    model = Sequential()
    model.add(Dense(12, input_dim=8, activation="relu"))
    model.add(Dense(8, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    # model.fit(X, Y, epochs=200, batch_size=50)

    # # 첫번째 사람의 데이터를 넣어 예측
    # print(model.predict([[6, 148, 72, 35, 0, 33.6, 0.627, 50]]))

    # print(model.evaluate(testX, testY))

    # model 정확도를 높이기 위해 데이터 정규화 하기 (데이터 Scale 조절) ex) Min-Max 정규화 (min값은 0으로 max값은 1로 만들어줌)
    # tip) Sklearn의 scaler 이용하기 (Min-Max 정규화와 값이 비슷하긴한데 같은건 아님!)
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    testX = scaler.fit_transform(testX)

    model.fit(X, Y, epochs=200, batch_size=50)
    print(model.evaluate(testX, testY))
