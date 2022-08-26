# 220418 기계학습프로그래밍(강교수님)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

if __name__ == '__main__':
    # # and 연산(두 비트 모두 1이면 1, 그렇지 않으면 0)
    # x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    # y = [[1, 0], [1, 0], [1, 0], [0, 1]]
    #
    # model = Sequential()
    # model.add(Dense(2, input_dim=2, kernel_initializer="normal", activation="softmax"))
    # model.summary()
    # model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    #
    # model.fit(x, y, epochs=200)
    # print(model.predict([[0, 0]]))
    # print(model.predict(x)) # 답 (0, 0, 0, 1) 맞게 예측된다. accuracy가 1.0000이니까.

    # xor 연산(두 비트가 다르면 1, 같으면 0)
    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[1, 0], [0, 1], [0, 1], [1, 0]]

    clf = Sequential()
    clf.add(Dense(512, input_dim=2, activation="sigmoid"))
    clf.add(Dense(2, activation="softmax"))
    # clf.summary()
    clf.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    clf.fit(x, y, epochs=1000)
    print(clf.predict(x))