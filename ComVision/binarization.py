import cv2
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # 임계값(threshold)
    # 밝기 값이 T 이상이면 1 아니면 0
    # src_img = cv2.imread("./image/Lenna.png")
    # gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    # threshold = 120

    # 직접 구현한 것
    # bin_img = gray.copy()
    # for y in range(bin_img.shape[0]):
    #     for x in range(bin_img.shape[1]):
    #         if bin_img[y, x] > threshold:
    #             bin_img[y, x] = 255
    #         else:
    #             bin_img[y, x] = 0
    # cv2.imshow("binarization", bin_img)

    # opencv 함수
    # ret_val, bin_img2 = cv2.threshold(gray, threshold, 255, cv2.THRESH_OTSU)
    # cv2.imshow("binarization2", bin_img2)
    # print(ret_val)

    # cv2.imshow("Original", src_img)
    # cv2.imshow("gray", gray)




    # 브로콜리와 당근을 구분하기
    src_img = cv2.imread("./image/c_b.png")
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    # ret_val, bin_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_OTSU)
    # cv2.imshow("binarization", bin_img)

    g_channel = src_img[:, :, 1]
    r_channel = src_img[:, :, 2]
    # cv2.imshow("g", g_channel)
    # cv2.imshow("r", r_channel)

    roi_g = g_channel[200:300, 250:340]
    roi_r = r_channel[87:168, 33:124]
    # cv2.imshow("roi", roi_g)


    # histo = np.bincount(roi_g.ravel(), minlength=256)
    # plt.plot(histo)
    # plt.show()

    ret_val, bin_img_r = cv2.threshold(r_channel, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("binarization_r", bin_img_r)
    ret_val, bin_img_g = cv2.threshold(g_channel, 150, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("binarization_g", bin_img_g)

    # bitwise_and 사용
    bin_img_g = cv2.cvtColor(bin_img_g, cv2.COLOR_GRAY2BGR) # 3채널로 만들어준다
    bin_img_r = cv2.cvtColor(bin_img_r, cv2.COLOR_GRAY2BGR) # 3채널로 만들어준다
    src_img = cv2.bitwise_and(src_img, bin_img_g)
    src_img = cv2.bitwise_and(src_img, bin_img_r)

    # 마스킹을 직접 구현
    # for y in range(bin_img.shape[0]):
    #     for x in range(bin_img.shape[1]):
    #         if bin_img[y, x] == 0:
    #             src_img[y, x] = [0, 0, 0]

    cv2.imshow("Original", src_img)




    cv2.waitKey(0)
    cv2.destroyAllWindows()