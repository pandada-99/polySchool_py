import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('image/Lenna.png')
    # print(src.shape)  # (512, 512, 3) == (Row(height), Col(width), Color Channel)


    blue = [255, 0, 0]
    green = [0, 255, 0]
    red = [0, 0, 255]
    white = [255, 255, 255]


    # Pixel 값 접근
    # print(src[100][200])
    # src[100][200] = [255, 255, 255]
    # print(src[100][200])


    # x좌표는 col값, y좌표는 row값
    # src[200, 0:512] = white
    # src[100:, 300] = blue


    # image Crop
    # face = src[240:400, 217:375]  # 얕은 복사
    face = src[240:400, 217:375].copy()  # 깊은 복사 Deep copy
    face[:, :, 0] = 255
    """
    # Color = [B, G, R]
    ➢ img[y, x, 0] → Blue 채널의 값
    ➢ img[y, x, 1] → Green 채널의 값
    ➢ img[y, x, 2] → Red 채널의 값
    """
    # cv2.imshow("Lena_face", face)


    # Color Channel
    b = src[:, :, 0]
    g = src[:, :, 1]
    r = src[:, :, 2]
    rgb_img = cv2.merge((r, g, b))
    # cv2.imshow("rgb", rgb_img)


    # 색 공간 변환
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray", gray)
    gray_2 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    # cv2.imshow("Color", gray_2)
    # print(gray_2[100][245])  # B, G, R 채널의 값이 모두 같은 값으로 채워져 있다


    # Mean Filter 적용
    # kernel1 = np.ones((3, 3), np.float32) / 9  # mean
    kernel1 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # 자기자신
    # kernel2 = np.ones((5, 5), np.float32) / 25  # mean
    kernel2 = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])  # 옆으로 한칸 이동 (내 자리에 내 옆자리 픽셀의 값 넣기)
    dst1 = cv2.filter2D(src, -1, kernel1)
    dst2 = cv2.filter2D(src, -1, kernel2)
    # cv2.imshow("Mean Filter1", dst1)
    # cv2.imshow("Mean Filter2", dst2)


    # Sharpening 선명도를 높여준다
    kernel3 = np.array([[-1, -1, -1], [-1, 17, -1], [-1, -1, -1]]) / 9
    dst3 = cv2.filter2D(src, -1, kernel3)
    cv2.imshow("Sharpening", dst3)


    # Smoothing 선명도를 낮춰준다
    dst4 = cv2.GaussianBlur(src, (5, 5), 3)
    cv2.imshow("Gaussian", dst4)
    dst5 = cv2.bilateralFilter(src, 5, 75, 75)  # 엣지를 잃어버리지 않으면서 노이즈 제거에 유용
    cv2.imshow("BilateralFilter", dst5)


    cv2.imshow("source", src)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    