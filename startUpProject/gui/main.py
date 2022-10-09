import cv2
import os
import numpy as np
from model.yolo_class import classes

nms_boxes = {}

def yolo(score_threshold, nms_threshold):
    # YOLO 네트워크 불러오기
    net = cv2.dnn.readNet(f"model/aiways_20000.weights", "model/aiways.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    # output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # GPU 사용
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    # 클래스의 갯수만큼 랜덤 RGB 배열을 생성
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # 이미지의 높이, 너비, 채널 받아오기
    height, width, channels = frame_origin.shape

    # 네트워크에 넣기 위한 전처리
    blob = cv2.dnn.blobFromImage(frame_origin, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # 전처리된 blob 네트워크에 입력
    net.setInput(blob)

    # 결과 받아오기
    outs = net.forward(output_layers)

    # 각각의 데이터를 저장할 리스트 생성 및 초기화
    class_ids = []
    confidences = []
    boxes = []

    re_class = []

    nms_boxes.clear()

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.1:
                # 탐지된 객체의 너비, 높이 및 중앙 좌표값 찾기
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # 객체의 사각형 테두리 중 좌상단 좌표값 찾기
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # print('│' + " YOLO ".center(90, '─') + '│')
    # 후보 박스(x, y, width, height) 출력
    # print(f"│boxes: {boxes}")
    # print(f"│confidences: {confidences}")

    # 노이즈 제거 (Non Maximum Suppression) (겹쳐있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)

    # NMS 을 통해 걸러진 박스의 인덱스 출력
    # print(f"│indexes: ", end='')
    # for index in indexes:
    #     print(index, end=' ')
    # print()

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            class_name = classes[class_ids[i]]

            # class_name == "person" 일때 box crop 해서 저장

            re_class.append(class_name)


            # 중복된 객체를 이름 뒤 숫자를 추가하여 구분
            class_name += '_1'
            num = 1
            while class_name in nms_boxes.keys():
                num += 1
                class_name = class_name[:-1] + str(num)

            # 프레임에 작성할 텍스트 및 색깔 지정
            label = f"{class_name}: {confidences[i]:.2f}"
            color = colors[class_ids[i]]

            # 프레임에 사각형 테두리 그리기 및 텍스트 쓰기
            cv2.rectangle(frame_drawn, (x, y), (x + w, y + h), color, 2)
            cv2.rectangle(frame_drawn, (x - 1, y), (x + len(class_name) * 13 + 80, y - 25), color, -1)
            cv2.putText(frame_drawn, label, (x, y - 8), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)

            # 탐지된 객체의 정보 출력 및 nms_boxex 에 저장
            print('{0}│'.format(
                f"│ [{class_name}] conf: {confidences[i]} / x: {x} / y: {y} / width: {w} / height: {h}".ljust(91, ' ')))
            nms_boxes[class_name] = [x, y, w, h]

    return re_class

switch = True

if __name__ == '__main__':
    webcam = cv2.VideoCapture(1)

    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    while webcam.isOpened():
        status, frame = webcam.read()

        if status:
            cv2.imshow("test", frame)

        if cv2.waitKey(1) == ord('c'):
            cv2.destroyWindow("test")
            cv2.imwrite("img/img.png", frame)
            frame_origin = cv2.imread("img/img.png")
            frame_drawn = frame_origin.copy()

            class_name = yolo(score_threshold=0.4, nms_threshold=0.4)

            cv2.imshow("test2", frame_drawn)
            print(class_name)
            cv2.waitKey(0)
            cv2.destroyWindow("test2")

        if cv2.waitKey(1) == ord('v'):
            break

    webcam.release()
    cv2.destroyAllWindows()
