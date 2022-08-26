import cv2
from functools import wraps
import time

import numpy as np

lastsave = 0


# (두 점 사이의 유클리드 거리 계산)
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)


# https://wjh2307.tistory.com/21
# 눈 감기(함수) + 자는거 판단(부정확)
def close_counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        global lastsave
        # print(f"during close: {time.time() - lastsave}")
        if time.time() - lastsave > 5:
            lastsave = time.time()
            tmp.count = 0
        return func(*args, **kwargs)

    tmp.count = 0
    return tmp


class eye_calculation:
    def __init__(self):
        """Initialization"""
        self.both_ER_ratio_avg = 0
        self.clahe = cv2.createCLAHE(clipLimit=2.0,
                                     tileGridSize=(8, 8))

    # 눈 비율 값 계산
    def ER_ratio(self, eye_point):
        # 얼굴 특징점 번호 사진 참조
        A = distance(eye_point[1], eye_point[5])
        B = distance(eye_point[2], eye_point[4])
        C = distance(eye_point[0], eye_point[3])
        return (A + B) / (2.0 * C)

    def eye_close(self, left_eye, right_eye):
        left_ER = self.ER_ratio(left_eye)
        right_ER = self.ER_ratio(right_eye)

        avg = round((left_ER + right_ER) / 2, 2)
        self.both_ER_ratio_avg = avg
        return avg < 0.3

    def draw_eye_close_ratio(self, img, color=(0, 255, 0)):
        cv2.putText(img, f"{self.both_ER_ratio_avg}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    def img_Preprocessing(self, img_frame):
        # Gaussian Pyramid: An image pyramid is a collection of images - all arising from a single original image - that are successively downsampled until some desired stopping point is reached.
        re_size = cv2.pyrDown(np.mean(img_frame, axis=2).astype("uint8"))

        # Tophat: The top-hat filter is used to enhance bright objects of interest in a dark background.
        filterSize = (160, 100)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)
        topHat = cv2.morphologyEx(re_size, cv2.MORPH_TOPHAT, kernel)  # 밝기가 높은것을 부각 시켜준다

        # CLAHE : # Equalizes the histogram of a grayscale image using Contrast Limited Adaptive Histogram Equalization.
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(16, 16))
        clahe = clahe.apply(topHat)

        histEqual = cv2.equalizeHist(clahe)
        ####To del
        composed = histEqual
        ####
        return re_size, composed




    @close_counter
    def close(self, img, color=(0, 0, 255)):
        cv2.putText(img, "close", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
