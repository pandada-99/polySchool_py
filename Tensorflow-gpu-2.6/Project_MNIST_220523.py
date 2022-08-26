from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets.mnist import load_data
import tensorflow as tf

if __name__ == '__main__':
    model = Sequential()
    model.add(Dense(512, input_dim=784, activation="relu"))
    model.add(Dense(10, activation="softmax")) # "softmax"는 10개 출력의 합이 1이 되게 만든다 (정규화) 확률을 보겠다!
    model.summary()

    model.compile(loss="categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])

    (train_data, train_label), (test_data, test_label) = load_data()

    train_data = train_data.reshape(60000, 784)
    test_data = test_data.reshape(10000, 784)

    train_label = tf.keras.utils.to_categorical(train_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기

    model.fit(train_data, train_label, epochs=10, batch_size=200)