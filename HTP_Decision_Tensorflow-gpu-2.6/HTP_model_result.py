import cv2
import numpy as np
import os

if __name__ == '__main__':
    classes = []
    f = open('classes.txt', 'r')
    classes = [line.strip() for line in f.readlines()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    success = 0
    for num in range(100):
        result_list = []
        for name in ['house', 'tree', 'person']:
            path = f"./data/HTP_paper/{name}_copy/"
            name_list = os.listdir(path)
            img = cv2.imread(path + name_list[num])
            if img.shape[0] > img.shape[1]:
                img = cv2.resize(img, (595, 842))
            else:
                img = cv2.resize(img, (842, 595))

            height, width, channels = img.shape
            blob = cv2.dnn.blobFromImage(img, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True, crop=False)

            yolo_model = cv2.dnn.readNet("./data/backup_ver3/custom_best.weights", "./data/backup_ver3/custom.cfg")
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
                    if confidence > 0.4:
                        centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                        w, h = int(vec85[2] * width), int(vec85[3] * height)
                        x, y = int(centerx - w / 2), int(centery - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            # 노이즈 제거 (Non Maximum Suppression) (겹쳐 있는 박스 중 상자가 물체일 확률이 가장 높은 박스만 남겨둠)
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.4)

            if len(indexes) > 0:
                i = confidences.index(max(confidences))
                x, y, w, h = boxes[i]

                # box 크기가 a4용지 크기보다 커지는걸 방지
                if x < 0: x = 0;
                if y < 0: y = 0;
                if x + w > width: w = width - x;
                if y + h > height: h = height - y;

                text = str(classes[class_ids[i]]) + "%.2f" % confidences[i]
                confi = "%.2f" % confidences[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
                cv2.putText(img, text, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, colors[class_ids[i]], 2)

                # box에 center 점 그리기
                center = (int(x + (w / 2)), int(y + (h / 2)))
                box_center_x = center[0]
                box_center_y = center[1]
                cv2.circle(img, center, 5, (255, 0, 255), 2)
                # print(f'중심점은 {center}')

                # box크기 비율 알기
                전체크기 = width * height
                디텍팅크기 = w * h
                비율 = 디텍팅크기 / 전체크기
                size = "%.2f" % 비율
                # print("비율 is", "%.2f" % 비율)

                result = [num, classes[class_ids[i]], float(confi), x, y, w, h, box_center_x, box_center_y, float(size), width, height]
                result_list.append(result)
                # print(result)
            else:
                result = ['fail']
                result_list.append(result)
                # print('탐지된 물체가 없습니다.')

        print(result_list)
        house_result = result_list[0]
        tree_result = result_list[1]
        person_result = result_list[2]

        if house_result[0] == 'fail' or house_result[1] != 'house':
            print(f"{num}번째 house detection fail")
            continue
        if tree_result[0] == 'fail' or tree_result[1] != 'tree':
            print(f"{num}번째 tree detection fail")
            continue
        if person_result[0] == 'fail' or person_result[1] != 'draw_person':
            print(f"{num}번째 person detection fail")
            continue

        # =============================================================================================
        house_place = []
        tree_place = []
        person_place = []

        if house_result[10] == 842: # 가로 방향
            if 0 <= house_result[7] <= 280:
                house_place.append('left')
            elif 280 < house_result[7] <= 562:
                house_place.append('center')
            else:
                house_place.append('right')

            if 0 <= house_result[8] <= 198:
                house_place.append('up')
            elif 198 < house_result[8] <= 397:
                house_place.append('center')
            else:
                house_place.append('down')

        if house_result[10] == 595: # 세로 방향
            if 0 <= house_result[7] <= 198:
                house_place.append('left')
            elif 198 < house_result[7] <= 397:
                house_place.append('center')
            else:
                house_place.append('right')

            if 0 <= house_result[8] <= 280:
                house_place.append('up')
            elif 280 < house_result[8] <= 562:
                house_place.append('center')
            else:
                house_place.append('down')

        if tree_result[10] == 842: # 가로 방향
            if 0 <= tree_result[7] <= 280:
                tree_place.append('left')
            elif 280 < tree_result[7] <= 562:
                tree_place.append('center')
            else:
                tree_place.append('right')

            if 0 <= tree_result[8] <= 198:
                tree_place.append('up')
            elif 198 < tree_result[8] <= 397:
                tree_place.append('center')
            else:
                tree_place.append('down')

        if tree_result[10] == 595: # 세로 방향
            if 0 <= tree_result[7] <= 198:
                tree_place.append('left')
            elif 198 < tree_result[7] <= 397:
                tree_place.append('center')
            else:
                tree_place.append('right')

            if 0 <= tree_result[8] <= 280:
                tree_place.append('up')
            elif 280 < tree_result[8] <= 562:
                tree_place.append('center')
            else:
                tree_place.append('down')

        if person_result[10] == 842: # 가로 방향
            if 0 <= person_result[7] <= 280:
                person_place.append('left')
            elif 280 < person_result[7] <= 562:
                person_place.append('center')
            else:
                person_place.append('right')

            if 0 <= person_result[8] <= 198:
                person_place.append('up')
            elif 198 < person_result[8] <= 397:
                person_place.append('center')
            else:
                person_place.append('down')

        if person_result[10] == 595: # 세로 방향
            if 0 <= person_result[7] <= 198:
                person_place.append('left')
            elif 198 < person_result[7] <= 397:
                person_place.append('center')
            else:
                person_place.append('right')

            if 0 <= person_result[8] <= 280:
                person_place.append('up')
            elif 280 < person_result[8] <= 562:
                person_place.append('center')
            else:
                person_place.append('down')

        # =============================================================================================
        해석 = []

        # 위치 해석
        if house_place[0] == 'left':
            해석.append('내향적 열등감을 가지고 있다.')
        elif house_place[0] == 'right':
            해석.append('외향성 활동성을 가지고 있다.')

        if tree_place[0] == 'left':
            해석.append('자의식이 강하고 부끄러움이 많거나 내향적인 성격으로 과거로 퇴행하는 경향이 있다.')
        elif tree_place[0] == 'right':
            해석.append('지적만족을 강조하며 부정적 사고와 적개심을 가지는 경향이 있다.')

        if person_place[0] == 'left':
            해석.append('소극적이며 우울감을 가지고 있다.')
        elif person_place[0] == 'right':
            해석.append('이기적이며 공격적이고 분노가 높다.')

        if house_place[1] == 'up' or tree_place[1] == 'up' or person_place[1] == 'up':
            해석.append('통찰력이 부족하고 이치에 맞지 않는 낙천주의를 가지고 있다.')
        if house_place[1] == 'down' or tree_place[1] == 'down' or person_place[1] == 'down':
            해석.append('안정감을 가지지만 우울하고 위축되어 있으며 패배감이 짙다.')

        # 크기 해석
        if house_result[9] <= 0.33:
            해석.append('열등감, 무능력감을 가지고 있고 소심하며, 자아강도가 낮다.')
            if person_result[9] > 0.67:
                해석.append('가족보다는 자신을 더 중요시하는 경향이 있다.')
        elif 0.67 < house_result[9]:
            해석.append('과장되고 공격적이며 보상적 방어의 감정을 가지고 과잉행동을 하는 경향이 있다.')
        
        if tree_result[9] <= 0.33:
            해석.append('자신에 대해 열등감을 가지고 있고 무력감을 느끼고 있다.')
        elif 0.33 < tree_result[9] < 0.9:
            해석.append('자기확대의 욕구를 가지며 공상보다는 현실적인 활동에서 만족을 얻으려고 한다.')
        else:
            해석.append('통찰력이 부족하고 생활공간으로부터의 일탈과 회의를 느낀다.')
        
        if person_result[9] <= 0.33:
            해석.append('수축된 자아를 가지고 있고 환경을 다루는데 있어서 부적절하며 낮은 에너지 수순을 가진다.')
        elif 0.67 < person_result[9]:
            해석.append('자기를 증명하려고 노력하는 경향이 있다.')

        # =============================================================================================
        print(f'{name_list[num]}의 해석 \n', 해석)
        print(f"{num}번째 성공")
        success = success+1
    print(f'{success}set 성공')


        # cv2.imshow('HTP Object detection', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()