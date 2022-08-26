from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.datasets import cifar10
import tensorflow as tf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), strides=(1, 1),
                     activation='relu',
                     input_shape=(32, 32, 3),
                     padding='same')) # padding: 원본크기와 똑같이 만들어줘
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(32, (5, 5), activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    (train_data, train_label), (test_data, test_label) = cifar10.load_data()
    print(train_data.shape)
    print(test_data.shape)

    class_name = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog',
                  'horse', 'ship', 'truck']

    for i in range(10):
        plt.subplot(1, 10, i + 1)
        plt.imshow(train_data[i])
        plt.xlabel(class_name[train_label[i][0]])
    plt.show()

    # train_data = train_data.reshape(50000, 32, 32, 3)
    # train_label = tf.keras.utils.to_categorical(train_label, 10) # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기
    # test_data = test_data.reshape(10000, 32, 32, 3)
    # test_label = tf.keras.utils.to_categorical(test_label, 10)  # (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) 형태로 만들기
    # print(train_data.shape)
    # print(test_data.shape)

    model.fit(train_data, train_label, epochs=10, batch_size=200)

    print(model.evaluate(test_data, test_label))