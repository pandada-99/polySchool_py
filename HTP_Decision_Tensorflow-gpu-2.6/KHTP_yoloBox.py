import cv2
import numpy as np

if __name__ == '__main__':
    file_name = '5.jpg'
    classes = []
    f = open('classes.txt', 'r')
    classes = [line.strip() for line in f.readlines()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    img = cv2.imread(f"data/KHTP/{file_name}")

    # img 전처리 (cv2.threshold 이진화)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret_val, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)




    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True, crop=False)

    yolo_model = cv2.dnn.readNet("./data/backup_ver2/custom_2000.weights", "./data/backup_ver2/custom.cfg")
    # yolo_model = cv2.dnn.readNet("./data/backup/custom_best.weights", "./data/backup/custom.cfg")
    layer_names = yolo_model.getLayerNames()
    out_layers = [layer_names[i - 1] for i in yolo_model.getUnconnectedOutLayers()]

    yolo_model.setInput(blob)
    # output3는 감지 결과, 탐지된 개체에 대한 모든 정보와 위치를 제공
    output3 = yolo_model.forward(out_layers)

    class_ids, confidences, boxes = [], [], []
    for output in output3:
        for vec85 in output:
            scores = vec85[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                w, h = int(vec85[2] * width), int(vec85[3] * height)
                x, y = int(centerx - w / 2), int(centery - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    print("boxes is ", boxes)

    # 노이즈 제거 (Non Maximum Suppression) (겹쳐 있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indexes) > 0:
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                box = boxes[i]

                print(box)
                x, y, w, h = box

                # box 크기가 a4용지 크기보다 커지는걸 방지
                if x < 0: x = 0;
                if y < 0: y = 0;
                if x + w > width: w = width - x;
                if y + h > height: h = height - y;

                text = str(classes[class_ids[i]]) + "%.2f" % confidences[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
                cv2.putText(img, text, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)

                # box에 center 점 그리기
                center = (int(x + w / 2), int(y + h / 2))
                cv2.circle(img, center, 5, (255, 0, 255), 6)

                # box크기 비율 알기
                전체크기 = width * height
                디텍팅크기 = w * h
                비율 = 디텍팅크기 / 전체크기
                print("비율 is", "%.2f" % 비율)
    else:
        print('탐지된 물체가 없습니다.')




    cv2.imshow('KHTP Object detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()