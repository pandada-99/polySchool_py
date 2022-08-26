import cv2
import dlib
import numpy as np


def shape_to_np(shape, dtype="int"): #TODO 얼굴 랜드마크를 np.array로 만들어주는 함수
    # initialize the list of (x, y)-coordinates #TODO (x, y) 좌표를 넣을 리스트 초기화
    coords = np.zeros((68, 2), dtype=dtype) #TODO 68행 2열의 0으로 채워진 int array 생성
    # loop over the 68 facial landmarks and convert them #TODO 68개의 얼굴 랜드마크를 돌면서 array를 채울꺼임
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y) #TODO 68개의 얼굴 랜드마크를 돌면서 array를 채우는중
    # return the list of (x, y)-coordinates
    return coords #TODO (x, y) 좌표 리턴


def eye_on_mask(mask, side):
    points = [shape[i] for i in side] #TODO 왼쪽, 오른쪽눈에 속하는 랜드마크를 넣을 points list 만듬
    points = np.array(points, dtype=np.int32) #TODO list를 int array로 바꿈
    #TODO 여러 점의 좌표를 이용해 채워진 블록 다각형을 그린다 (mask = img파일 / points = 좌표 점들(x,y) / 255 = 색상(white)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask #TODO 왼쪽 혹은 오른쪽눈 좌표를 받아 흰색으로 채운 다각형 리턴



detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

left = [36, 37, 38, 39, 40, 41]
right = [42, 43, 44, 45, 46, 47]

cap = cv2.VideoCapture(0)
ret, img = cap.read()

kernel = np.ones((9, 9), np.uint8)


while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        mask = eye_on_mask(mask, left)
        mask = eye_on_mask(mask, right)
        mask = cv2.dilate(mask, kernel, 5)
        eyes = cv2.bitwise_and(img, img, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        eyes = cv2.GaussianBlur(eyes, (9, 9), 0)
        _, threshold = cv2.threshold(cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY), 70, 255, cv2.THRESH_BINARY)
        cv2.imshow('eye', cv2.resize(threshold, dsize=(800, 800)))

        mask2 = np.zeros(img.shape[:2], dtype=np.uint8)
        mask2 = eye_on_mask(mask2, left)
        mask2 = eye_on_mask(mask2, right)
        mask2 = cv2.dilate(mask2, kernel, 5)
        eyes2 = cv2.bitwise_and(img, img, mask=mask2)
        mask2 = (eyes2 == [0, 0, 0]).all(axis=2)
        eyes2[mask2] = [255, 255, 255]
        cv2.imshow('eye2', cv2.resize(eyes2, dsize=(800, 800)))


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()