import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.models import load_model
import tensorflow as tf

if __name__ == '__main__':
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(4, 4), strides=(4, 4), activation='relu', input_shape=(28, 28, 1), padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (4, 4), activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    tf.keras.layers.Dropout(0.2)
    model.add(Dense(10, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    (train_data, train_label), (test_data, test_label) = load_data()

    train_data = np.expand_dims(train_data, axis=-1)
    test_data = np.expand_dims(test_data, axis=-1)
    print(train_data.shape)
    print(test_data.shape)

    train_label = tf.keras.utils.to_categorical(train_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기
    test_label = tf.keras.utils.to_categorical(test_label, 10)  # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기

    # model.fit(train_data, train_label, epochs=10, batch_size=200)
    # model.save('./mnist_data/my_MNIST_CNN.h5')

    model = load_model('./mnist_data/my_MNIST_CNN.h5')
    print(model.evaluate(test_data, test_label))