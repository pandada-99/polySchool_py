import cv2
import numpy as np

def img_Contrast(img): # img 전처리 함수
    # -----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # -----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

    # -----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b))

    # -----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final

if __name__ == '__main__':

    # # Yolo 로드
    # net = cv2.dnn.readNet("data/backup/custom_best.weights", "custom.cfg")
    # classes = []
    # with open("classes.names", "r") as f:
    #     classes = [line.strip() for line in f.readlines()]
    # layer_names = net.getLayerNames()
    # output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    # colors = np.random.uniform(0, 255, size=(len(classes), 3))
    #
    # # 이미지 가져오기
    # img = cv2.imread("data/test/test_tree_1.png")
    # # img = cv2.resize(img, None, fx=0.4, fy=0.4)
    # height, width, channels = img.shape
    # print(height, width)
    #
    # # Detecting objects
    # blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    # net.setInput(blob)
    # outs = net.forward(output_layers)
    #
    # # 정보를 화면에 표시
    # class_ids = []
    # confidences = []
    # boxes = []
    # for out in outs:
    #     for detection in out:
    #         scores = detection[5:]
    #         class_id = np.argmax(scores)
    #         confidence = scores[class_id]
    #         if confidence > 0.5:
    #             # Object detected
    #             center_x = int(detection[0] * width)
    #             center_y = int(detection[1] * height)
    #             w = int(detection[2] * width)
    #             h = int(detection[3] * height)
    #             # 좌표
    #             x = int(center_x - w / 2)
    #             y = int(center_y - h / 2)
    #             boxes.append([x, y, w, h])
    #             confidences.append(float(confidence))
    #             class_ids.append(class_id)
    #
    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    #
    # font = cv2.FONT_HERSHEY_PLAIN
    # for i in range(len(boxes)):
    #     if i in indexes:
    #         x, y, w, h = boxes[i]
    #         label = str(classes[class_ids[i]])
    #         color = colors[i]
    #         cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    #         cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
    # cv2.imshow("Image", img)
    # print(boxes)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    file_name = 'HTP_tree_26.png'
    classes = []
    f = open('classes.txt', 'r')
    classes = [line.strip() for line in f.readlines()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    img = cv2.imread(f"data/HTP_tree/{file_name}")
    ##### test 이미지 전처리 하기 #####

    # cv2.createCLAHE 균일화
    # img = img_Contrast(img)

    # cv2.equalizeHist 균일화
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.equalizeHist(img)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # cv2.threshold 이진화
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret_val, img = cv2.threshold(img, 150, 255, cv2.THRESH_OTSU)
    ret_val, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # cv2.Canny
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.Canny(img, 0, 255)
    # img = 255 - img
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1.0/256, (448, 448), (0, 0, 0), swapRB=True, crop=False)

    yolo_model = cv2.dnn.readNet("data/backup/custom_best.weights", "custom.cfg")
    layer_names = yolo_model.getLayerNames()
    out_layers = [layer_names[i-1] for i in yolo_model.getUnconnectedOutLayers()]

    yolo_model.setInput(blob)
    output3 = yolo_model.forward(out_layers)

    class_ids, confidences, boxes = [], [], []
    for output in output3:
        for vec85 in output:
            scores = vec85[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                centerx, centery = int(vec85[0]*width), int(vec85[1]*height)
                w, h = int(vec85[2]*width), int(vec85[3]*height)
                x, y = int(centerx-w/2), int(centery-h/2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            box = boxes[i]
            text = str(classes[class_ids[i]])+"%.2f"%confidences[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), colors[class_ids[i]], 2)
            cv2.putText(img, text, (x, y+30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)



    print(box)
    x, y, w, h = box

    # box 크기가 a4용지 크기보다 커지는걸 방지
    if x < 0 : x = 0;
    if y < 0 : y = 0;
    if x+w > width : w = width-x;
    if y+h > height : h = height-y;
    print(x, y, w, h)

    img_test = cv2.imread(f"data/HTP_tree/{file_name}")
    height, width, t_channels = img_test.shape
    print(height, width)
    # cv2.circle(img_test, (50, 70), 5, (255, 0, 255), 6)
    # cv2.circle(img_test, (545, 70), 5, (255, 0, 255), 6)
    # cv2.circle(img_test, (50, 772), 5, (255, 0, 255), 6)
    # cv2.circle(img_test, (248, 491), 5, (255, 0, 255), 6)
    center = (int(x+w/2), int(y+h/2))
    print(center)
    전체크기 = width * height
    디텍팅크기 = w * h
    print(디텍팅크기)
    비율 = 디텍팅크기 / 전체크기
    print(비율)

    cv2.rectangle(img_test, (x, y), (x+w, y+h), (225, 0, 0), 2)
    cv2.circle(img_test, center, 5, (255, 0, 255), 6)
    cv2.imshow('test', img_test)



    cv2.imshow('Object detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()