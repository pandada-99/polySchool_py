from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.datasets.mnist import load_data
import tensorflow as tf

if __name__ == '__main__':
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), strides=(1, 1),
                     activation='relu',
                     input_shape=(28, 28, 1),
                     padding='same')) # padding: 원본크기와 똑같이 만들어줘
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    (train_data, train_label), (test_data, test_label) = load_data()

    train_data = train_data.reshape(60000, 28, 28, 1)
    train_label = tf.keras.utils.to_categorical(train_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기

    model.fit(train_data, train_label, epochs=10, batch_size=200)