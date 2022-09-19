import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    src_img = cv2.imread("./image/Unequalized_Hawkes_Bay_NZ.jpg")
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)


    # 밝기 히스토그램
    hist = [0] * 256
    for y in range(gray.shape[0]):
        for x in range(gray.shape[1]):
            hist[gray[y, x]] += 1
    print(hist)
    plt.subplot(1, 3, 1)
    plt.plot(hist)


    # Min-Max Normalization 정규화
    norm_img = gray.astype(np.float32)
    # print(norm_img.min()) # 114
    # print(norm_img.max()) # 208
    norm_img = (norm_img - norm_img.min()) / (norm_img.max() - norm_img.min())
    cv2.imshow("Norm Img", norm_img)


    # Histogram Equalization 평탄화
    opencv_eq = cv2.equalizeHist(gray)
    cv2.imshow("opencv_eq", opencv_eq)

    hist2 = [0] * 256
    for y in range(opencv_eq.shape[0]):
        for x in range(opencv_eq.shape[1]):
            hist2[opencv_eq[y, x]] += 1
    print(hist2)
    plt.subplot(1, 3, 2)
    plt.plot(hist2)
    
    # Numpy 라이브러리 사용한 히스토그램
    hist3 = np.bincount(opencv_eq.flatten(), minlength=256)
    print(hist3)
    plt.subplot(1, 3, 3)
    plt.plot(hist3)

    plt.show()


    cv2.waitKey(0)
    cv2.destroyAllWindows()