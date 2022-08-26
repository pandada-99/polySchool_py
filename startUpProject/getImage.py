import cv2
import os

for i in ['aaa.mp4', 'bbb.mp4']:
    filepath = 'C:/Users/AI-00/PycharmProjects/startUpProject/video/' + i
    video = cv2.VideoCapture(filepath)

    if not video.isOpened():
        print("Could not Open :", filepath)
        exit(0)

    # 불러온 비디오 파일의 정보 출력
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    print("length :", length)
    print("width :", width)
    print("height :", height)
    print("fps :", fps)

    try:
        if not os.path.exists(i[:-4] + "_video"):
            os.makedirs(i[:-4] + "_video")
    except OSError:
        print('Error: Creating directory. ' + i[:-4])

    count = 0

    while (True):
        ret, image = video.read()
        if (ret == 1):
            cv2.imwrite(i[:-4] + "_video/" + i[:-4] + "_frame%d.jpg" % count, image)
            print('Saved frame number :', str(int(video.get(1))))
            count += 1
            # cv2.imshow('gray', image)
            # cv2.waitKey(50)
            # cv2.destroyAllWindows()
        else: break

    video.release()