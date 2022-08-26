import cv2
from keras.models import load_model
import numpy as np

# 모델 input -> (0, 28, 28, 0), 배경 검정색, 숫자 흰색, 정규화(나누기 255)하기
if __name__ == "__main__":
    filename = "C:/Users/AI-00/PycharmProjects/ComVision/mnist_model.h5"
    model = load_model(filename)
    # model.summary()

    ###################################################################################################################
    src = cv2.imread("number.png")
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    test_img = cv2.erode(gray, None, iterations=2)
    _, test_img = cv2.threshold(test_img, 0, 255, cv2.THRESH_OTSU)
    test_img = 255 - test_img

    # 블롭 구하기
    n_blob, label_img, stats, centroids = cv2.connectedComponentsWithStats(test_img)
    # blob의 갯수(배경 포함), 레이블 된 이미지, 박스 좌표(x, y, w, h, area), 중심 좌표
    print(n_blob)  # 총 blob 갯수
    blob = []
    for i in range(1, n_blob):
        if (stats[i][3]) > 50:
            blob.append(stats[i][:4])