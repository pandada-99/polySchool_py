import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import seaborn as sns

# 데이터 이미지로 연속 보기
def show_image(img, label):
    plt.imshow(255-img, cmap="gray")
    # print(label)
    plt.show()

# 데이터 분포 확인
def show_data_values(labels):
    count_value = np.bincount(labels)
    print(count_value) # 데이터가 고루 분포되어있는지 갯수확인(너무 한쪽으로 몰려있으면 학습 안함, 데이터가 많은쪽으로만 말해도 정확도가 높으니까)
    plt.bar(np.arange(0, 10), count_value)
    plt.xticks(np.arange(0, 10))
    plt.grid()
    plt.show()


if __name__ == '__main__':
    path = "c:/Users/AI-00/PycharmProjects/Tensorflow-gpu-2.6/data/mnist.npz"
    (train_set, train_label), (test_set, test_label) = tf.keras.datasets.mnist.load_data(path)

    # # 데이터 이미지로 연속 보기
    # userInput = ""
    # index = 0
    # while userInput != "q":
    #     show_image(train_set[index], train_label[index])
    #     index += 1
    #     userInput = input("next?: ")

    # # 데이터 분포 확인
    # show_data_values(train_label)
    # show_data_values(test_label)

    train_set = train_set.reshape(len(train_set), 784)
    # 학습할 때만 쓴다.
    # clf = RandomForestClassifier()
    # clf.fit(train_set, train_label)
    # joblib.dump(clf, "rf_mnist.pkl")

    # 저장한 모델 불러오기
    clf = joblib.load("./data/rf_mnist.pkl")
    # print(clf.predict(train_set[0:1]))

    # test_set에 대하여 검증
    test_set_2 = test_set.reshape(len(test_set), 784)
    predict_test = clf.predict(test_set_2)
    # print(type(predict_test))
    # print(clf.score(test_set_2, test_label)) # 만개의 test_set중에 얼마나 맞췄는지

    # 과제: 오답노트(틀린부분 뽑아내기)
    # for i in range(len(predict_test)):
    #     if predict_test[i] == test_label[i]:
    #         continue
    #     else:
    #         print(f"예측값은 {predict_test[i]}, 정답은 {test_label[i]}입니다.")
    #         show_image(test_set[i], test_label[i])

    # print(clf.predict(test_set[0:40]))
    # print(test_label[0:40])


    # 과제: confusion matrix (오차 행렬)
    # 2차원 배열 만들기 = [[1, 2], [3, 4],...[8, 9]]
    # confusion = [[0 for i in range(10)] for j in range(10)]
    # print(confusion)
    # 2차원 배열 접근하기
    # print(confusion[9][8])

    # for i in range(len(predict_test)):
    #     for j in range(10):
    #         if test_label[i] == j:
    #             if predict_test[i] == 0:
    #                 confusion[j][0] = confusion[j][0]+1
    #             elif predict_test[i] == 1:
    #                 confusion[j][1] = confusion[j][1]+1
    #             elif predict_test[i] == 2:
    #                 confusion[j][2] = confusion[j][2]+1
    #             elif predict_test[i] == 3:
    #                 confusion[j][3] = confusion[j][3]+1
    #             elif predict_test[i] == 4:
    #                 confusion[j][4] = confusion[j][4]+1
    #             elif predict_test[i] == 5:
    #                 confusion[j][5] = confusion[j][5]+1
    #             elif predict_test[i] == 6:
    #                 confusion[j][6] = confusion[j][6]+1
    #             elif predict_test[i] == 7:
    #                 confusion[j][7] = confusion[j][7]+1
    #             elif predict_test[i] == 8:
    #                 confusion[j][8] = confusion[j][8]+1
    #             elif predict_test[i] == 9:
    #                 confusion[j][9] = confusion[j][9]+1
    # print(confusion)

    confusion = [[0 for i in range(10)] for j in range(10)]

    for i in range(len(predict_test)):
        for j in range(10):
            if test_label[i] == j:
                for k in range(10):
                    if predict_test[i] == k:
                        confusion[j][k] = confusion[j][k]+1
    print(confusion)


    # Heatmap 그리기 ####################################################################################################

    # 백분율로 표시하기
    predict_list = [0]*10

    for i in range(len(predict_test)):
        for j in range(10):
            if predict_test[i] == j:
                predict_list[j] = predict_list[j] + 1

    print(predict_list)

    # confusion2 = [[0 for i in range(10)] for j in range(10)]
    # for i in range(10):
    #     for j in range(10):
    #         confusion2[i][j] = confusion[i][j]/predict_list[i]
    #
    # confusion3 = [[0 for i in range(10)] for j in range(10)]
    # for i in range(10):
    #     for j in range(10):
    #         confusion3[i][j] = round(confusion2[i][j], 3)
    #         confusion3[i][j] = (confusion3[i][j])*100
    #
    # print(confusion3)

    confusion2 = [[0 for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(10):
            confusion2[i][j] = (confusion[i][j] / predict_list[i]) # 전체 0으로 예측한 값의 합을 나눠줌

    print(confusion2)

    plt.figure(figsize=(10, 5))
    sns.heatmap(confusion2, linewidths=.5, annot=True, cmap="YlGnBu", cbar=False, vmax=2, fmt=".2%")
    plt.title('Heatmap by plt.pcolor()', fontsize=20)
    plt.title('Confusion matrix', fontsize=15)
    plt.xlabel('test_predict')
    plt.ylabel('test_label')
    plt.show()


    # Heatmap 그리기2 ###################################################################################################
    confusion2 = [[0 for i in range(10)] for j in range(10)]

    for i in range(len(test_label)) :
        l = test_label[i]
        p = predict_test[i]
        confusion2[l][p] += 1

    print(confusion2)