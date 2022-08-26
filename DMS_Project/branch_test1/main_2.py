import math

import joblib
from sklearn.tree import DecisionTreeClassifier
import pickle
import numpy as np
import cv2
import time
from my_mark_detector import MarkDetector, FaceDetector
from branch_test1.pose_estimator import PoseEstimator
from calculation import eye_calculation
from functools import wraps

lastsave = 0

print(__doc__)
print("OpenCV version: {}".format(cv2.__version__))

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
SKYBLUE = (255, 255, 0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ALL = list(range(0, 68))
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INLINE = list(range(51, 68))
FACE_OUTLINE = list(range(0, 17))
NOTHING = list(range(0, 0))
MARK_INDEX = RIGHT_EYE + LEFT_EYE + MOUTH_INLINE

frame_cnt = 0
frame_sum = 0
frame_avg = 0
# video_capture = cv2.VideoCapture("./branch_test1.mp4")  # 사진
video_capture = cv2.VideoCapture(0)  # 카메라

width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

pose_estimator = PoseEstimator(img_size=(height, width), model_path="../assets/model.txt")

# 3. Introduce a mark detector to detect landmarks.
face_detector = FaceDetector()
mark_detector = MarkDetector(save_model="../assets/shape_predictor_68_face_landmarks.dat")  # 경로 확인 필수!!

eye_calc = eye_calculation()

def test_D_ndarray(land):
    dis = []
    분모 = distance(land[29], land[33])
    dis.append(distance(land[33], land[0]) / 분모)
    dis.append(distance(land[33], land[16])/ 분모)
    dis.append(distance(land[33], land[31])/ 분모)
    dis.append(distance(land[33], land[35])/ 분모)
    dis.append(distance(land[33], land[36])/ 분모)
    dis.append(distance(land[33], land[39])/ 분모)
    dis.append(distance(land[33], land[42])/ 분모)
    dis.append(distance(land[33], land[45])/ 분모)

    dis.append(distance(land[39], land[42])/ 분모)
    dis.append(distance(land[36], land[39])/ 분모)
    dis.append(distance(land[42], land[45])/ 분모)
    dis.append(distance(land[31], land[35])/ 분모)
    dis.append(distance(land[28], land[33])/ 분모)
    return np.array(dis).reshape(1,-1)

def test_D1(land):
    result = []
    # 왼쪽 눈
    a = distance(land[37],land[41])
    b = distance(land[38],land[40])
    c = distance(land[36],land[39])
    result.append((a + b) / c * 2)
    # 오른쪽 눈
    a = distance(land[43], land[47])
    b = distance(land[44], land[46])
    c = distance(land[42], land[45])
    result.append((a + b) / c * 2)
    # 코
    a = distance(land[27], land[33])
    b = distance(land[31], land[35])
    result.append(b/a)
    # 입
    a = distance(land[51], land[57])
    b = distance(land[48], land[54])
    result.append(a/b)

    return np.array(result).reshape(1,-1)

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)

count_head = 0
count_mouth = 0
max_count = 50
min_count = 0

def leftRight(mark):
    num = mark[3][0][0] - mark[2][0][0]
    if num >= 6: return 0
    elif -6 < num < 6: return 2
    else: return 1

def degree(mark):
    radian = np.arctan2((distance(mark[1][0], mark[3][0])), (distance(mark[3][0], mark[2][0])))
    degree = radian * 180 / math.pi
    if 80 >= degree >= 70: return 1
    else: return 0

def head(mark):
    # 고개 안숙였을 때 (현재)
    a = 1.5 / 5
    # 고개 숙였을 때 (1초 뒤)
    b = distance(mark[27], mark[30]) / distance(mark[30], mark[8])

    if (b > a * 1.8): return 1
    else: return 0

def mouth(mark):
    # 입을 다물었을 때 (평상시)
    a = 1 / 2
    # 하품할 때
    b = distance(mark[62], mark[66]) / distance(mark[60], mark[64])

    if (b > a * 1.5): return 1
    else: return 0

# loaded_model = pickle.load(open("./classifiermaybe99.pkl", 'rb'))
loaded_model = joblib.load("./classifiermaybe99.pkl")

if video_capture.isOpened():
    print("camera is ready")
    while True:
        frame_cnt += 1
        start_t = time.time()
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        ret, img = video_capture.read()

        # img = cv2.flip(img, 1) # 시나리오 측정할때는 좌우 반전 풀고 실행
        # img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 적외선 카메라 사용시


        # img, cmpos = eye_calc.img_Preprocessing(img)  # 프레임별 이미지 전처리
        face_box = face_detector.get_faceboxes(img)  # 전처리한 이미지에서 얼굴 검출
        if face_box is not None:
            landmark = mark_detector.get_marks(img, face_box)  # 얼굴에서 랜드마크 추출 type:list

            landmark_ndarray = np.array(landmark, dtype=np.float32)  # 파라미터 타입은 numpy.ndarray으로 해야함
            # 추가로 solve_pose_by_68_points 내부 함수 중 cv2.solvePnP의 인자중 랜드마크는 np.float32로 해주어야 한다
            pose = pose_estimator.solve_pose_by_68_points(landmark_ndarray)

            # # 눈 감는거 + 자는거(부 정확함) 판단=======================================================
            eye_close_status = eye_calc.eye_close(landmark[36:42], landmark[42:48])
            if eye_close_status:
                eye_calc.close(img)
                if eye_calc.close.count >= 7:
                    cv2.putText(img, "SLEEPING   !!!", (100, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)
            # # 눈 감김 판단 끝 =======================================================================


            # # 시각화 ===============================================================================
            # # 육면체를 보고싶다면?
            # pose_estimator.draw_annotation_box(img, pose[0], pose[1], color=GREEN)

            # # x, y, z 축 보고 싶다면?
            axis = pose_estimator.get_axis(img, pose[0], pose[1])  # 축에 대한 데이터를 쓰고 싶은데 어디있는지 모름 ㅎ
            # axis = [[[RED_x RED_y]],[[GREEN_x GREEN_y]],[[BLUE_x BLUE_y]],[[CENTER_x CENTER_y]]]
            # --> BLUE(정면) GREEN(아래) RED(좌측) CENTER(중심)
            pose_estimator.draw_axes(img, pose[0], pose[1])

            axis = axis.tolist()  # numpy array를 list로 변환
            # 고개 돌리는지 확인
            # print(axis, type(axis))
            # num = axis[3][0][0] - axis[2][0][0] # CENTER_x - BLUE_x => 양수면 오른쪽 음수면 왼쪽을 보고있음
            # print(axis[3][0][0] - axis[2][0][0])
            if leftRight(axis) == 0:
                cv2.putText(img, "RIGHT", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)
            elif leftRight(axis) == 2:
                cv2.putText(img, "FACADE", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)
            else:
                cv2.putText(img, "LEFT", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)

            # # 고개 내렸는지 확인
            # radian2 = np.arctan2((distance(axis[1][0], axis[3][0])), (distance(axis[3][0], axis[2][0])))
            # degree2 = radian2 * 180 / math.pi
            #
            # radian = np.arctan2((axis[1][0][1] - axis[3][0][1]), (axis[3][0][0] - axis[2][0][0]))
            # degree = radian * 180 / math.pi
            #
            # print(degree, "/", degree2)
            #
            # if degree(axis) == 1:
            #     cv2.putText(img, "FACADE", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)
            # else:
            #     cv2.putText(img, "UP&DOWN", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)

            # 함수 호출
            if (head(landmark) == 1):
                if count_head < max_count:
                    count_head += 1
            else:
                if count_head > min_count:
                    count_head -= 1
            if count_head > 25:
                cv2.putText(img, "sleep_head!!", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, SKYBLUE, 2)
            # print(distance(landmark[27], landmark[30]) / distance(landmark[30], landmark[8]))

            # 함수 호출
            if (mouth(landmark) == 1):
                if count_mouth < max_count:
                    count_mouth += 1
            else:
                if count_mouth > min_count:
                    count_mouth -= 1
            if count_mouth > 35:
                cv2.putText(img, "Yawn!!", (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, SKYBLUE, 2)

            # out = test_D_ndarray(landmark)

            # print(loaded_model.predict(out))


            # # 얼굴 랜드마크 보고 싶다면
            mark_detector.draw_marks(img, landmark[0:], color=GREEN)

            # # 얼굴 detect box 보고 싶다면?
            # detection_box = [face_box.left(), face_box.top(),
            #                  face_box.right(), face_box.bottom()]
            # mark_detector.draw_box(img, [detection_box], box_color=BLUE)



        frame_sum += int(1. / (time.time() - start_t))
        if frame_cnt == 3:
            frame_avg = round(frame_sum / frame_cnt)
            frame_cnt = 0
            frame_sum = 0
        cv2.putText(img, f"FPS:{frame_avg}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED, 2)
        cv2.imshow("img", img)

cv2.destroyAllWindows()
video_capture.release()
