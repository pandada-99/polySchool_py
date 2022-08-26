import cv2

cap = cv2.VideoCapture('C:/Users/AI-00/PycharmProjects/startUpProject/video/판콜에이내복액.mp4')

while True:
    ret, img = cap.read()

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break