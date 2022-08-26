import cv2
import os

for i in [0, 1, 2]:
    filepath = 'C:/Users/AI-00/PycharmProjects/DMS_Project/Master_220603/test_data/'
    for j in range(10):
        filename = str(i) + "/" + str(i) + "-" + "0" + str(j) + ".mp4"
        video = cv2.VideoCapture(filepath + filename) #'' 사이에 사용할 비디오 파일의 경로 및 이름을 넣어주도록 함

        if not video.isOpened():
            print("Could not Open :", filepath+filename)
            exit(0)

        # 영상 평균으로 resize 합시다
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # 가로
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # 세로

        # 불러온 비디오 파일의 정보 출력
        # length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        # width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        # height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # fps = video.get(cv2.CAP_PROP_FPS)

        # w = []
        # h = []
        # for i in range(30):
        #     w.append(width)
        #     h.append(height)
        #
        # w_avg = sum(w)/len(w)
        # h_avg = sum(h)/len(h)
        # print(w_avg, h_avg) # 1920.0, 1080.0

        # print("length :", length)
        # print("width :", width)
        # print("height :", height)
        # print("fps :", fps)

        count = 0

        while (True):
            ret, image = video.read()
            if (ret == 1):
                cv2.imwrite(filepath + "img/" + str(i) + "/" + str(j) + "_" + "frame{0}".format(count) + ".jpg", image)
                print('Saved frame number :', str(int(video.get(1))))
                count += 1
            else: break

        video.release()

