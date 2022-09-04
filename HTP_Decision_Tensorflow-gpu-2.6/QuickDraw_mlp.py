import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import torch

np.set_printoptions(threshold=sys.maxsize)

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)


if __name__ == '__main__':
    # data load (hospital)
    df_hospital = np.load('./data/full_numpy_bitmap_hospital.npy')
    df_hospital = pd.DataFrame(df_hospital)  # shape(167448, 784)
    # df_hospital = df_hospital[0:30000]
    # label 만들어주기 (hospital is '0')
    df_hospital_label = np.zeros(167448)
    df_hospital_label = pd.DataFrame(df_hospital_label)

    # data load (broccoli)
    df_broccoli = np.load('./data/full_numpy_bitmap_broccoli.npy')
    df_broccoli = pd.DataFrame(df_broccoli)  # shape(132826, 784)
    # df_broccoli = df_broccoli[0:30000]
    # label 만들어주기 (broccoli is '1')
    df_broccoli_label = np.ones(132826)
    df_broccoli_label = pd.DataFrame(df_broccoli_label)

    # data load (simply)
    # data_sp = pd.read_json('./data/full_simplified_hospital.ndjson', lines=True)
    # data_draw = data_sp['drawing']

    # data 합치기
    df_train = pd.concat([df_hospital, df_broccoli])
    df_label = pd.concat([df_hospital_label, df_broccoli_label])

    # one hot encoding
    train_label = tf.keras.utils.to_categorical(df_label, 2)

    # train와 test로 data 나누기
    x_train, x_test, y_train, y_test = train_test_split(df_train, df_label, test_size=0.3, stratify=df_label, random_state=34)


    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    # x_train = np.array(x_train)
    # x_train = torch.Tensor(x_train)
    # y_train = np.array(y_train)
    # y_train = torch.Tensor(y_train)

    # x_train = x_train.reshape(42000, 28, 28)
    # x_test = x_test.reshape(18000, 28, 28)
    # x_train = np.expand_dims(x_train, axis=-1)
    # x_test = np.expand_dims(x_test, axis=-1)
    # x_train = np.expand_dims(x_train, axis=1)
    # x_test = np.expand_dims(x_test, axis=1)
    # print(x_train.shape, x_train.ndim)
    # print(x_test.shape, x_test.ndim)

    # model 만들기
    mlp = Sequential()
    mlp.add(Dense(1024, input_dim=784, activation="relu"))
    mlp.add(Dense(512, activation="relu"))
    mlp.add(Dense(1, activation="sigmoid"))
    mlp.summary()
    mlp.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    MY_EPOCH = 10
    MY_BATCHSIZE = 800
    mlp.fit(x_train, y_train, epochs=MY_EPOCH, batch_size=MY_BATCHSIZE)

    filename = "./quickdraw_data/mlp_hd1024_512_e(10).h5"
    mlp.save(filename)

    print(mlp.evaluate(x_test, y_test))