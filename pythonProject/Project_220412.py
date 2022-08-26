# 220412 인공지능개론(강교수님)
from matplotlib import pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':
    n = 100

    X = 6 * (np.random.rand(n, 1)) - 3
    Y = 0.5 * X**2 + X + 2 + np.random.rand(n, 1)

    plt.scatter(X, Y, s=3)

    poly_feat = PolynomialFeatures(degree=2)
    X_poly = poly_feat.fit_transform(X)

    lr = LinearRegression()
    lr.fit(X_poly, Y)

    plt.scatter(X, Y, s=3)




    # X = np.linspace(0, 2*math.pi, 12)
    # Y = np.sin(X)
    # plt.scatter(X, Y)
    #
    # # numpy 배열은 ','가 없음
    # print(X)
    # print(X.reshape(-1, 1)) # numpy옵션 reshape할때 -1,1을 주면 차원이 하나 더 늘어남.
    #
    # X = X.reshape(-1, 1)
    # lr = LinearRegression()
    # lr.fit(X, Y)


    # X = []
    # Y = []
    #
    # # X는 360도를 30도 간격으로 나눔(12개)
    # for i in range(0,361,30):
    #     X.append(i * math.pi / 180)
    #     Y.append(math.sin(i * math.pi / 180))
    #
    # lr = LinearRegression()
    #
    # X_2d = []
    # for i in X:
    #     X_2d.append([i])
    #
    # lr.fit(X_2d, Y)
    #
    # plt.scatter(X, Y)
    # plt.plot(X, lr.predict(X_2d))
    # plt.show()