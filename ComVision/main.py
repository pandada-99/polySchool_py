import cv2

if __name__ == '__main__':
    img = cv2.imread("image/Lenna.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    w_width = 200
    w_height = 200

    for y in range(100):
        for x in range(100):
            crop = gray[y:y+w_width, x:x+w_width]
            cv2.imshow("crop_img", crop)
            key = cv2.waitKey(33)

            if key == 27: # esc
                cv2.destroyAllWindows()
                exit(0)

    white = [255, 255, 255]
    blue = [255, 0, 0]
    green = [0, 255, 0]
    red = [0, 0, 255]

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(gray[200, 200])
    # cv2.imshow("gray", gray)

    # gray를 다시 color로 바꿀수있나?
    gray_2 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    # print(gray_2[200, 200])
    gray_2[100, 100:200] = red
    # cv2.imshow("gray_2", gray_2)

    # HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)

    # HSV 채널 분리
    v = hsv[:, :, 2]
    # cv2.imshow("hsv-v", v)

    b, g, r = cv2.split(img)
    # cv2.imshow("Blue", b)
    # cv2.imshow("Green", g)
    # cv2.imshow("Red", r)

    # img = cv2.merge( [r, g, b])

    # img[200, :] = green
    # img[:, 100] = blue

    face = img[240:400, 217:375].copy()
    face[:, :, 2] = 255
    # cv2.imshow("Lenaface", face)
    # cv2.imwrite("face_red.jpg", face)

    cv2.imshow("Lena", img)
    cv2.waitKey(0) # 이미지에 어떤 입력이 올 때까지 무한으로 기다림, key를 주면 창이 닫힘
    cv2.destroyAllWindows()