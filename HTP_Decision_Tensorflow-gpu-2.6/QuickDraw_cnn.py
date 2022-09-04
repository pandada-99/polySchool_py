import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from sklearn.model_selection import train_test_split
import torch

np.set_printoptions(threshold=sys.maxsize)

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)


if __name__ == '__main__':
    # data load (hospital)
    df_hospital = pd.read_json('./data/full_simplified_hospital.ndjson', lines=True)  # shape(167448, 6)
    # drawing값만 뽑아내기
    df_hospital = pd.DataFrame(df_hospital)
    df_hospital = df_hospital.iloc[:]['drawing']  # shape(167448, )
    print(df_hospital.shape, df_hospital.dtypes)
    # for i in range(167448):
    #     df_hospital =+ df_hospital[i]

    # label 만들어주기 (hospital is '0')
    df_hospital_label = np.zeros(167448)
    # df_hospital_label = pd.DataFrame(df_hospital_label)  # shape(167448, 1)


    # data load (broccoli)
    df_broccoli = pd.read_json('./data/full_simplified_broccoli.ndjson', lines=True)  # shape(132826, 6)
    # drawing값만 뽑아내기
    df_broccoli = pd.DataFrame(df_broccoli)
    df_broccoli = df_broccoli.iloc[:]['drawing']  # shape(132826, )
    print(df_broccoli.shape, df_broccoli.dtypes)
    # for i in range(132826):
    #     df_broccoli =+df_broccoli[i]

    # label 만들어주기 (broccoli is '1')
    df_broccoli_label = np.ones(132826)
    # df_broccoli_label = pd.DataFrame(df_broccoli_label)  # shape(132826, 1)


    # data 합치기
    df_train = np.concatenate([df_hospital, df_broccoli])
    # print(df_train[0])
    # print(df_train[1])
    # print(df_train[2])
    df_label = np.concatenate([df_hospital_label, df_broccoli_label])
    # print(df_label[0])
    # print(df_label[130000])
    # print(df_label[200000])

    # print(len(df_train[0]), df_train[0])
    # print(len(df_train[1]), df_train[1])
    # print(len(df_train[2]), df_train[2])
    # for i in range(300274):
    #     for j in range(len(df_train[i])):
    #         for k in range(len(df_train[i][j])):
    #             for x in range(len(df_train[i][j][k])):
    #                 simply = np.zeros([28])
    #                 df_train[i][j][k][x] = df_train[i][j][k][x] + simply

    print(df_train[0])
    print(df_train.shape)
    print(df_label.shape)
    exit()

    # for i in range(167448):
    #     a = np.array([df_train][i], dtype=float)
    #     df_train = df_train.append(a)
    df_train = np.array(df_train)
    df_train = torch.Tensor(df_train)
    df_label = np.array(df_label)
    df_label = torch.Tensor(df_label)

    # one hot encoding
    train_label = tf.keras.utils.to_categorical(df_label, 2)

    # train와 test로 data 나누기
    x_train, x_test, y_train, y_test = train_test_split(df_train, df_label, test_size=0.3, stratify=df_label, random_state=34)

    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    # x_train = x_train.reshape(42000, 28, 28)
    # x_test = x_test.reshape(18000, 28, 28)
    x_train = np.expand_dims(x_train, axis=-1)
    x_test = np.expand_dims(x_test, axis=-1)
    x_train = np.expand_dims(x_train, axis=1)
    x_test = np.expand_dims(x_test, axis=1)
    print(x_train.shape, x_train.ndim)
    print(x_test.shape, x_test.ndim)


    # model 만들기
    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=(5, 5), strides=(4, 4), activation='relu', input_shape=(210191, 784, 1), padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(32, (5, 5), activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(16, activation='relu'))
    tf.keras.layers.Dropout(0.2)
    model.add(Dense(1, activation='sigmoid'))
    model.summary()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10, batch_size=800)

    print(model.evaluate(x_test, y_test))

    filename = "quickdraw_mlp/cnn_hd64_32_16_e(10).h5"
    # model.save(filename)