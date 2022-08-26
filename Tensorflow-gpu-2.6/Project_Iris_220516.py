from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    df = pd.read_csv("./data/Iris.csv")
    df.drop(["Id"], axis=1, inplace=True)
    # print(df.head())
    # print(df.info())
    # print(df.describe())

    # Species를 숫자로 만들기 =============================================================================================
    e = LabelEncoder()
    df2 = e.fit_transform(df["Species"])
    # print(df2)
    df.drop(["Species"], axis=1, inplace=True)
    df["Species"] = df2
    print(df.head())

    # # 칼럼들의 상관 관계 (히트맵 시각화) ====================================================================================
    # plt.figure(figsize=(6, 6))
    # seaborn.heatmap(df.corr(), annot=True, linewidths=0.1)
    # plt.show()

    # 신경망 학습 ========================================================================================================
    dataset = df.values
    X = dataset[1:, :-1]
    Y = dataset[1:, -1]
    Y = tf.keras.utils.to_categorical(Y, 3) # (0, 1, 0) 형태로 만들기 => One-Hot Encoding(정답만 1로 나머지는 0으로)
    # print(Y)

    # test는 20%, train은 80%로 값을 랜덤으로 나눈다
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y,
                                                        test_size=0.2,
                                                        shuffle=True)
    # print(train_X, train_Y)

    model = Sequential()
    model.add(Dense(12, input_dim=4, activation="swish"))
    model.add(Dense(3, activation="softmax"))
    model.summary()

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(train_X, train_Y, epochs=300)

    print(model.evaluate(test_X, test_Y))