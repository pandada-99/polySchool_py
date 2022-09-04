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

np.set_printoptions(threshold=sys.maxsize)

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)


if __name__ == '__main__':
    # data load (hospital)
    df_hospital = np.load('./data/full_numpy_bitmap_hospital.npy')
    df_hospital = pd.DataFrame(df_hospital)  # shape(167448, 784)
    # label 만들어주기 (hospital is '0')
    df_hospital_label = np.zeros(167448)
    df_hospital_label = pd.DataFrame(df_hospital_label)

    # data load (broccoli)
    df_broccoli = np.load('./data/full_numpy_bitmap_broccoli.npy')
    df_broccoli = pd.DataFrame(df_broccoli)  # shape(132826, 784)
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

    # model 만들기
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=(4, 4), strides=(4, 4), activation='relu', input_shape=(210191, 784, 1), padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    # model.add(Conv2D(32, (4, 4), activation='relu', padding='same'))
    # model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(32, activation='relu'))
    tf.keras.layers.Dropout(0.2)
    model.add(Dense(10, activation='sigmoid'))
    model.summary()
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10, batch_size=800)
    print(model.evaluate(x_test, y_test))
    # model.save('./mnist_data/my_MNIST_CNN.h5')