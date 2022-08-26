import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

def make_model():
    mlp = Sequential()
    mlp.add(Dense(512, input_dim=784, activation="relu"))
    mlp.add(Dense(10, activation="softmax"))
    mlp.summary()
    mlp.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    return mlp

MY_EPOCH = 30
MY_BATCHSIZE = 200
def train(model, x, y):
    history = model.fit(x, y, epochs=MY_EPOCH, batch_size=MY_BATCHSIZE)

    filename = "./data/mlp_hd512_e({0}).h5".format(MY_EPOCH)
    model.save(filename)

    return history


if __name__ == "__main__":
    (train_set, train_label), (test_set, test_label) = tf.keras.datasets.mnist.load_data("mnist.npz") # "mnist.npz" 안적으면 인터넷에서 다운로드함

    train_set = train_set.reshape(60000, 784) # 이미지를 1차원으로 쭉 펴줌 (randomforest에 넣었던것 처럼) 28*28 => 1*784
    test_set = test_set.reshape(10000, 784) # 이미지를 1차원으로 쭉 펴줌 (randomforest에 넣었던것 처럼)

    train_label = tf.keras.utils.to_categorical(train_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기
    test_label = tf.keras.utils.to_categorical(test_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기

    # mlp = make_model()
    #
    # train_history = []
    # test_history = []
    # for i in range(1, 11):
    #     del mlp
    #     mlp = make_model()
    #     train(mlp, train_set, train_label)
    #     MY_EPOCH = i*5
    #     train_history.append(train(mlp, train_set, train_label))
    #     test_history.append(mlp.evaluate(test_set, test_label, batch_size=MY_BATCHSIZE))

    # for i in range(1, 11):
    #     del mlp
    #     MY_EPOCH = i*5
    #     filename = "./data/mlp_hd512_e({0}).h5".format(MY_EPOCH)
    #     mlp = load_model(filename)
    #     print("train set acc: {0}".format(mlp.evaluate(train_set, train_label)))
    #     print("test set acc: {0}".format(mlp.evaluate(test_set, test_label)))

    mlp = Sequential()
    mlp.add(Dense(1024, input_dim=784, activation="relu"))
    mlp.add(Dense(512, activation="relu"))
    mlp.add(Dense(10, activation="softmax"))
    mlp.summary()
    mlp.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    MY_EPOCH = 35
    MY_BATCHSIZE = 200
    # mlp.fit(train_set, train_label, epochs=MY_EPOCH, batch_size=MY_BATCHSIZE)

    filename = "./mnist_data/mlp_hd1024_512_e(35).h5"
    # mlp.save(filename)
    mlp = load_model(filename)

    print(mlp.evaluate(test_set, test_label))
