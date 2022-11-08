import cv2
import numpy as np
import os

if __name__ == '__main__':
    ####################################################################################################################
    path_house = "./data/HTP_paper/house/"
    house_list = os.listdir(path_house)
    for name in house_list:
        file_name = f'{name}'

        img_h = cv2.imread(f"data/HTP_paper/house/{file_name}")
        print(img_h.shape)
        if img_h.shape[0] > img_h.shape[1]:
            img_h = cv2.resize(img_h, (595, 842))
        else:
            img_h = cv2.resize(img_h, (842, 595))
        print(img_h.shape)

        # img 전처리 (cv2.threshold 이진화)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ret_val, img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        height, width, channels = img_h.shape
        blob = cv2.dnn.blobFromImage(img_h, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True, crop=False)


        # house 모델
        classes = []
        f = open('./data/backup_house/house_classes.names', 'r')
        classes = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        yolo_model_h = cv2.dnn.readNet("./data/backup_house/house_custom_1000.weights", "./data/backup_house/house_custom.cfg")
        layer_names = yolo_model_h.getLayerNames()
        out_layers = [layer_names[i - 1] for i in yolo_model_h.getUnconnectedOutLayers()]

        yolo_model_h.setInput(blob)
        # output3는 감지 결과, 탐지된 개체에 대한 모든 정보와 위치를 제공
        output3 = yolo_model_h.forward(out_layers)

        class_ids, confidences, boxes = [], [], []
        for output in output3:
            for vec85 in output:
                scores = vec85[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                    w, h = int(vec85[2] * width), int(vec85[3] * height)
                    x, y = int(centerx - w / 2), int(centery - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        print("boxes is ", boxes)

        # 노이즈 제거 (Non Maximum Suppression) (겹쳐 있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

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
                    cv2.rectangle(img_h, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
                    cv2.putText(img_h, text, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)

                    # box에 center 점 그리기
                    center = (int(x + w / 2), int(y + h / 2))
                    cv2.circle(img_h, center, 5, (255, 0, 255), 6)

                    # box크기 비율 알기
                    전체크기 = width * height
                    디텍팅크기 = w * h
                    비율 = 디텍팅크기 / 전체크기
                    print("비율 is", "%.2f" % 비율)
        else:
            print('탐지된 house가 없습니다.')

        cv2.imshow('split_house', img_h)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




    ####################################################################################################################
    path_tree = "./data/HTP_paper/tree/"
    tree_list = os.listdir(path_tree)
    for name in tree_list:
        file_name = f'{name}'

        img_t = cv2.imread(f"data/HTP_paper/tree/{file_name}")
        print(img_t.shape)
        if img_t.shape[0] > img_t.shape[1]:
            img_t = cv2.resize(img_t, (595, 842))
        else:
            img_t = cv2.resize(img_t, (842, 595))
        print(img_t.shape)

        # img 전처리 (cv2.threshold 이진화)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ret_val, img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        height, width, channels = img_t.shape
        blob = cv2.dnn.blobFromImage(img_t, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True, crop=False)

        # tree 모델
        classes = []
        f = open('./data/backup_tree/tree_classes.names', 'r')
        classes = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        yolo_model_t = cv2.dnn.readNet("./data/backup_tree/tree_custom_1000.weights", "./data/backup_tree/tree_custom.cfg")
        layer_names = yolo_model_t.getLayerNames()
        out_layers = [layer_names[i - 1] for i in yolo_model_t.getUnconnectedOutLayers()]

        yolo_model_t.setInput(blob)
        # output3는 감지 결과, 탐지된 개체에 대한 모든 정보와 위치를 제공
        output3 = yolo_model_t.forward(out_layers)

        class_ids, confidences, boxes = [], [], []
        for output in output3:
            for vec85 in output:
                scores = vec85[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                    w, h = int(vec85[2] * width), int(vec85[3] * height)
                    x, y = int(centerx - w / 2), int(centery - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        print("boxes is ", boxes)

        # 노이즈 제거 (Non Maximum Suppression) (겹쳐 있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

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
                    cv2.rectangle(img_t, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
                    cv2.putText(img_t, text, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)

                    # box에 center 점 그리기
                    center = (int(x + w / 2), int(y + h / 2))
                    cv2.circle(img_t, center, 5, (255, 0, 255), 6)

                    # box크기 비율 알기
                    전체크기 = width * height
                    디텍팅크기 = w * h
                    비율 = 디텍팅크기 / 전체크기
                    print("비율 is", "%.2f" % 비율)
        else:
            print('탐지된 tree가 없습니다.')

        cv2.imshow('split_tree', img_t)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




    ####################################################################################################################
    path_person = "./data/HTP_paper/person/"
    person_list = os.listdir(path_person)
    for name in person_list:
        file_name = f'{name}'

        img_p = cv2.imread(f"data/HTP_paper/person/{file_name}")
        print(img_p.shape)
        if img_p.shape[0] > img_p.shape[1]:
            img_p = cv2.resize(img_p, (595, 842))
        else:
            img_p = cv2.resize(img_p, (842, 595))
        print(img_p.shape)

        # img 전처리 (cv2.threshold 이진화)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ret_val, img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        height, width, channels = img_p.shape
        blob = cv2.dnn.blobFromImage(img_p, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True, crop=False)

        # person 모델
        classes = []
        f = open('./data/backup_person/person_classes.names', 'r')
        classes = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        yolo_model_p = cv2.dnn.readNet("./data/backup_person/person_custom_1000.weights", "./data/backup_person/person_custom.cfg")
        layer_names = yolo_model_p.getLayerNames()
        out_layers = [layer_names[i - 1] for i in yolo_model_p.getUnconnectedOutLayers()]

        yolo_model_p.setInput(blob)
        # output3는 감지 결과, 탐지된 개체에 대한 모든 정보와 위치를 제공
        output3 = yolo_model_p.forward(out_layers)

        class_ids, confidences, boxes = [], [], []
        for output in output3:
            for vec85 in output:
                scores = vec85[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.1:
                    centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                    w, h = int(vec85[2] * width), int(vec85[3] * height)
                    x, y = int(centerx - w / 2), int(centery - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        print("boxes is ", boxes)

        # 노이즈 제거 (Non Maximum Suppression) (겹쳐 있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

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
                    cv2.rectangle(img_p, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
                    cv2.putText(img_p, text, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)

                    # box에 center 점 그리기
                    center = (int(x + w / 2), int(y + h / 2))
                    cv2.circle(img_p, center, 5, (255, 0, 255), 6)

                    # box크기 비율 알기
                    전체크기 = width * height
                    디텍팅크기 = w * h
                    비율 = 디텍팅크기 / 전체크기
                    print("비율 is", "%.2f" % 비율)
        else:
            print('탐지된 person이 없습니다.')

        cv2.imshow('split_person', img_p)
        cv2.waitKey(0)
        cv2.destroyAllWindows()