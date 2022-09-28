import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    src_img = cv2.imread("./image/Lenna.png")
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)


    # # histogram을 수동으로 구해봄
    # hist = [0] * 256
    #
    # for y in range(gray.shape[0]):
    #     for x in range(gray.shape[1]):
    #         hist[gray[y, x]] += 1
    #
    # print(hist)
    # plt.plot(hist)
    # plt.show()


    # # OpenCv 라이브러리 사용
    # hist2 = cv2.calcHist(images=[gray],
    #                      channels=[0],
    #                      mask=None,
    #                      histSize=[256],
    #                      ranges=[0, 256])
    # hist2 = hist2.flatten()
    # hist2 = hist2.astype(np.int32)
    # print(hist2)
    # plt.plot(hist2)
    # plt.show()


    # # numpy 이용하기
    # hist2, bins = np.histogram(gray.ravel(), 256, [0, 256])
    # # 더 빠르다
    # hist2 = np.bincount(gray.flatten(), minlength=256)
    #
    # print(hist2)
    # plt.plot(hist2)
    # plt.show()

    """
    정규화 => 데이터를 정규화해서 비슷한 스케일로 맞춰주겠다. (확률 때문에 0과 1사이에 넣는거지 다른 스케일로 넣어도 상관x)
    왜필요하냐? 키(160~180) 몸무게(50~80)가 주는 영향이 똑같은데 키가 숫자가 커서 더 큰 영향을 줌
    에시로 min-maz Normalization는 최소값을 0으로 최대값을 1로 만들어서 중간값을 그 사이로 넣기
    """

    # Min-Max Normalization 직접 구현
    norm_img = gray.astype(np.float32)
    # print(norm_img.min()) # 25
    # print(norm_img.max()) # 245
    norm_img = (norm_img - norm_img.min()) / (norm_img.max() - norm_img.min())
    # cv2.imshow("Norm Img", norm_img)

    norm_img *= 255
    norm_img = norm_img.astype(np.uint8)
    # norm_hist = np.bincount(norm_img.flatten(), minlength=256)
    # print(norm_hist)
    # plt.plot(norm_hist)
    # plt.show()
    #
    # # opencv noramalize 함수 사용
    # norm_opencv = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
    # cv2.imshow("Noralize_opencv", norm_opencv)


    # Histogram Equalization 히스토그램 평탄화
    # 히스토그램을 구한다.
    histo = np.bincount(norm_img.ravel(), minlength=256)
    # 누적 히스토그램 계산
    cdf = histo.cumsum()

    M = norm_img.shape[0]
    N = norm_img.shape[1]
    h_v = (cdf - cdf.min()) / (M * N - cdf.min()) * 255

    he_img = norm_img.copy()
    for y in range(M):
        for x in range(N):
            he_img[y, x] = h_v[norm_img[y, x]]
    cv2.imshow("norm", norm_img) # Min-Max 정규화
    cv2.imshow("hist_eq_img", he_img) # 히스토그램 평탄화

    # opencv의 히스토그램 평탄화 사용
    opencv_eq = cv2.equalizeHist(gray)
    cv2.imshow("opencv_eq", opencv_eq) # opencv의 함수 사용한 히스토그램 평탄화


    # color영상 히스토그램 평탄화
    b = src_img[:, :, 0]
    g = src_img[:, :, 1]
    r = src_img[:, :, 2]

    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)

    color_eq = cv2.merge((b, g, r))
    cv2.imshow("color_eq", color_eq) # opencv의 함수 사용한 color영상 히스토그램 평탄화


    cv2.imshow("Original", src_img)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()