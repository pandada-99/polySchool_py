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


def contouring(thresh, mid, img, right=False): #TODO 동공에 빨간 원 그리는 함수
    #TODO 외각선 검출 (thresh = 입력 영상 /
    #  cv2.RETR_EXTERNAL = 외각선 검출 모드(계층 정보 x, 바깥 외곽선만 검출합니다. 단순히 리스트로 묶어줍니다.) /
    #  cv2.CHAIN_APPROX_NONE = 외각선 근사화 방법(윤곽점들의 모든 점을 반환합니다.)
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    try:
        cnt = max(cnts, key=cv2.contourArea) #TODO cv2.contourArea => 외각선이 감싸는 영역의 면적 반환
        M = cv2.moments(cnt) #TODO cv2.moments => 이미지 모멘트를 계산하고 딕셔너리 형태로 리턴 ('m10', 'm00', 'm01'공간 모멘트)
        cx = int(M['m10'] / M['m00']) #TODO 중심의 x좌표
        cy = int(M['m01'] / M['m00']) #TODO 중심의 y좌표
        if right: #TODO True값을 주면 cx에 mid 더하기
            cx += mid
        # TODO (img = img파일 / (cx, cy) = 원의 중심 좌표 / 4 = 원의 반지름 / (0, 0, 255) = 색상(red) / 2 = 선 두께)
        cv2.circle(img, (cx, cy), 4, (0, 0, 255), 2)
    except:
        pass #TODO try에서 오류가 발생하면 pass


detector = dlib.get_frontal_face_detector() #TODO 얼굴 디텍트하는 라이브러리 받아오기
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') #TODO 랜드마크 주는 라이브러리 받아오기

left = [36, 37, 38, 39, 40, 41] #TODO 왼쪽눈 랜드마크 index
right = [42, 43, 44, 45, 46, 47]  #TODO 오른쪽눈 랜드마크 index

cap = cv2.VideoCapture(0) #TODO 웹켐 실행
ret, img = cap.read()
thresh = img.copy() #TODO thresh = 영상 이미지 카피

cv2.namedWindow('image') #TODO 'image'라는 새로운 윈도우창 띄움
kernel = np.ones((9, 9), np.uint8) #TODO 9행 9열의 1으로 채워진 양수(0~255) array 생성


def nothing(x):
    pass







#TODO cv2.createTrackbar => 트랙바 생성 ('threshold' = 트랙바 이름 / 'image' = 트랙바를 생성할 창 이름 /
# 0 = 트랙바 위치 초기값 / 255 = 트랙바 최댓값(최솟값은 항상 0) / nothing = 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름(그저 pass만 할것....))
cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

while (True): #TODO 라이브로 들어오는 비디오를 프레임별로 캡쳐하고 이를 화면에 디스플레이
    #TODO cap.read() => 재생되는 비디오의 한 프레임씩 읽는다 (프레임을 제대로 읽었다면 ret값이 True, 실패하면 ret값이 False / 읽은 프레임은 img)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #TODO 프레임을 흑백으로 변환
    rects = detector(gray, 1) #TODO 얼굴 전체를 인식
    for rect in rects:
        shape = predictor(gray, rect) #TODO 얼굴의 랜드마크 잡기
        shape = shape_to_np(shape) #TODO 얼굴 랜드마크를 np.array로 만들어줌
        mask = np.zeros(img.shape[:2], dtype=np.uint8) #TODO 프레임이랑 똑같은 크기의 검정 틀을 만든다
        mask = eye_on_mask(mask, left) #TODO 왼쪽눈 좌표를 받아 흰색으로 채운 다각형 리턴
        mask = eye_on_mask(mask, right) #TODO 오른쪽눈 좌표를 받아 흰색으로 채운 다각형 리턴
        #TODO cv2.dilate => 이미지 변환(객체 외각 팽창) (mask = 입력영상 / kernel = 구조 요소 커널(9, 9) / 5 = 반복해서 몇번 실행할지)
        mask = cv2.dilate(mask, kernel, 5)
        #TODO cv2.bitwise_and => 각 픽셀에 대해 AND연산, 프레임을 합쳐서 모두 흰곳만 흰곳으로 표현 (mask = 적용 영역 지정) /
        #  눈만 뽑아낸 mask를 합쳐 둘다 흰색으로 표현된 곳만 흰색으로 보임
        eyes = cv2.bitwise_and(img, img, mask=mask)
        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        # eyes = cv2.GaussianBlur(eyes, (9, 9), 0)
        # _, threshold = cv2.threshold(cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY), 50, 255, cv2.THRESH_BINARY)
        cv2.imshow('eyeeeees', cv2.resize(eyes, dsize=(1200, 1200)))


        mask = (eyes == [0, 0, 0]).all(axis=2)
        eyes[mask] = [255, 255, 255]
        mid = (shape[42][0] + shape[39][0]) // 2 #TODO 양 눈 안쪽의 중앙값(x 좌표)
        eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY) #TODO 눈 뽑아낸 프레임을 흑백으로 변환
        #TODO cv2.getTrackbarPos => 트랙바의 현재 위치 반환 ('threshold' = 트랙바 이름 / 'image' = 윈도우 이름)
        threshold = cv2.getTrackbarPos('threshold', 'image')
        #TODO cv2.threshold => 임계값 지원 함수 (eyes_gray = 입력 영상 / threshold = 사용자 지정 임계값 /
        #  255 = maxval(픽셀 문턱값보다 클 때 적용되는 최대값) / cv2.THRESH_BINARY = 픽셀값이 threshold_value 보다 크면 value, 작으면 0으로 할당)
        _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
        thresh = cv2.erode(thresh, None, iterations=2)  # 1 #TODO cv2.erode => 이미지 침식 (None = 커널 없음 / iterations = 반
        # 복 횟수)
        thresh = cv2.dilate(thresh, None, iterations=4)  # 2 #TODO cv2.dilate => 이미지 팽창 (None = 커널 없음 / iterations = 반복 횟수)
        #TODO cv2.medianBlur => 주변 픽셀들의 값들을 정렬하여 그 중앙값으로 픽셀 값을 대체 (thresh = 입력 영상 / 3 = 커널 크기(1보다 큰 홀수 지정))
        thresh = cv2.medianBlur(thresh, 3)  # 3
        # TODO cv2.bitwise_not => 색이 반대로 나타남
        thresh = cv2.bitwise_not(thresh)
        contouring(thresh[:, 0:mid], mid, img)
        contouring(thresh[:, mid:], mid, img, True)
        # for (x, y) in shape[36:48]:
        #     cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
    # show the image with the face detections + facial landmarks
    cv2.imshow('eyes', img)
    cv2.imshow("image", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #TODO 오픈한 cap 객체를 해제
cv2.destroyAllWindows() #TODO 생성한 윈도우 제거