import cv2
import numpy as np
import imutils
import win32file


class Camera:
    # Color
    __RED = (0, 0, 255)
    __GREEN = (0, 255, 0)
    __BLUE = (255, 0, 0)
    __YELLOW = (0, 255, 255)
    __SKYBLUE = (255, 255, 0)
    __PURPLE = (255, 0, 255)
    __WHITE = (255, 255, 255)
    __BLACK = (0, 0, 0)

    # Resolution
    __PIXELS = [(1920, 1080), (1440, 980), (1280, 720), (1040, 680), (900, 600),
                (640, 480)]  # 해상도 픽셀수가 커질수록 좋다(프레임 차이는 거의 없는거 같다)

    def __init__(self, path=0):
        self.PIXEL_NUMBER = 2
        self.RES_W = self.__PIXELS[self.PIXEL_NUMBER][0]
        self.RES_H = self.__PIXELS[self.PIXEL_NUMBER][1]
        print(f"pixel set ({self.__PIXELS[self.PIXEL_NUMBER][1]},{self.__PIXELS[self.PIXEL_NUMBER][0]})")
        try:
            self.cap = cv2.VideoCapture(path)
        except:
            print("Error opening video stream or file")

    def getFrameResize2ndarray(self, frame):
        return np.array(imutils.resize(frame, width=self.RES_W, height=self.RES_H))

    def getFrame2array(self, frame):
        pass

    def setPixels(self, resolution):
        print(f"H:{self.__PIXELS[resolution][1]} W{self.__PIXELS[resolution][0]}")
        return self.__PIXELS[resolution]

    def getRed(self):
        return self.__RED

    def getGreen(self):
        return self.__GREEN

    def getBlue(self):
        return self.__BLUE

    def getYellow(self):
        return self.__YELLOW

    def getSkyblue(self):
        return self.__SKYBLUE

    def getPurple(self):
        return self.__PURPLE

    def getWhite(self):
        return self.__WHITE

    def getBlack(self):
        return self.__BLACK


path = "C:/Users/AI-00/PycharmProjects/DMS_Project/master_220617/drive-download-20220627/"
filename = ["WIN_20220624_15_58_44_Pro", "WIN_20220624_15_49_03_Pro", "WIN_20220624_15_40_21_Pro",
            "WIN_20220624_15_29_33_Pro"]

print(__doc__)
video = path + filename[1] + ".mp4"
cm = Camera(path=video)  # path를 안하면 카메라 하면 영상

# line = []
# f = open(path + "final/" + filename[0] + "._final.txt", "r")
# while True:
#     c = f.readline()
#     if c == '':
#         break
#     line.append(c)
#
# line2 = []
# for i in range(len(line)):
#     a = line[i].split(',')
#     line2.append(a)

# f = open(path + "final/" + filename[0] + "._final.txt", "r")
# while True:
#     c = f.read()
#     if c == '' : break
#     print(c, end='')

f = open(path + "final/" + filename[1] + "._final.txt", "r")
frame_count = 0

while cm.cap.isOpened():
    ret, frame = cm.cap.read()

    #     for i in range(len(line)):
    #         a = line[i].split(',')
    #         if a[0] == frame_count:
    #             if a[1] == '1\n':
    #                 cv2.putText(frame, "sleep!!", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, Camera.getGreen(), 2)
    #         print(frame_count, '///', a[0])
    #     cv2.imshow("output", frame)
    #     key = cv2.waitKey(5)
    # if key == 27:
    #     cv2.destroyAllWindows()
    #     cm.cap.release()
    #     break

    if ret:
        frame_count += 1

    txt = f.readline().split(',')
    # print(txt)
    if txt[1] == ' 1\n':
        cv2.putText(frame, "sleep!!", (600, 200), cv2.FONT_HERSHEY_SIMPLEX, 8, cm.getGreen(), 2)

    # for i in range(len(line)):
    #     print(line2[i][1])
    #     if line2[i][1] == '1\n':
    #         cv2.putText(frame, "sleep!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, Camera.getGreen(), 2)

    cv2.imshow("output", frame)
    key = cv2.waitKey(5)
    if key == 27:
        cv2.destroyAllWindows()
        cm.cap.release()
        break