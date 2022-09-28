import cv2
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    src_img = cv2.imread("./image/Lenna.png")
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)


    # gradient
    # sobel 필터
    x_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    y_kernel = np.array([[1, 2, 1],
                         [0, 0, 0],
                         [-1, -2, -1]])
    k_size = 3
    row, col = gray.shape
    gradient = np.zeros((row-2, col-2), dtype=np.uint8)

    for y in range(row-2):
        for x in range(col-2):
            # 커널이 덮어지는 영역
            roi = gray[y:y+k_size, x:x+k_size]
            sx = np.sum(x_kernel * roi)
            sy = np.sum(y_kernel * roi)
            gradient[y, x] = np.sqrt(sx**2 + sy**2)
    # ret_val, gradient = cv2.threshold(gradient, 200, 255, cv2.THRESH_BINARY)
    cv2.imshow("gradient", gradient)


    # canny edge
    canny = cv2.Canny(src_img, 50, 200)
    cv2.imshow("canny", canny)



    cv2.imshow("Original", src_img)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()