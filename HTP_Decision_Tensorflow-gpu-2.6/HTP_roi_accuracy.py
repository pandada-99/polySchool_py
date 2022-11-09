import os
import json
import cv2

def gt_read(file_name):
    with open(f'{gt_path}{file_name}', 'r') as f:
        json_data = json.load(f)
    class_name = json_data[0]['annotations'][0]['label']
    c_x = int(json_data[0]['annotations'][0]['coordinates']['x'])
    c_y = int(json_data[0]['annotations'][0]['coordinates']['y'])
    w = int(json_data[0]['annotations'][0]['coordinates']['width'])
    h = int(json_data[0]['annotations'][0]['coordinates']['height'])
    x = c_x - (w//2)
    y = c_y - (h//2)
    return [class_name, x, y, w, h]

def pred_read(file_name):
    f = open(f'{pred_path}{file_name}', 'r')
    a = f.readline()
    if a == " ":
        return None
    class_name, confidence = a.split(', ')
    x, y, w, h = f.readline().split(', ')
    c_x, c_y = f.readline().split(', ')
    size = f.readline()
    confidence = confidence.replace("\n", "")
    h = h.replace("\n", "")
    c_y = c_y.replace("\n", "")
    return [class_name, float(confidence), int(x), int(y), int(w), int(h)]

def IoU(box1, box2):
    # box = (x1, y1, x2, y2)
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # obtain x1, y1, x2, y2 of the intersection
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # compute the width and height of the intersection
    w = max(0, x2 - x1 + 1)
    h = max(0, y2 - y1 + 1)

    inter = w * h
    iou = inter / (box1_area + box2_area - inter)
    return iou




if __name__ == '__main__':
    list_name = ['house', 'tree', 'person']
    result_list = []
    for name in list_name:
        gt_path = f"./data/HTP_paper/{name}_answer/"
        gt_box = os.listdir(gt_path)
        house_gt = [file for file in gt_box if file.endswith(".json")]
        house_img = [file for file in gt_box if file.endswith(".JPG")]

        pred_path = f"./data/HTP_paper/{name}_ver3_best/"
        pred_box = os.listdir(pred_path)
        house_pred = [file for file in pred_box if file.endswith(".txt")]

        # print(pred_read(house_pred[0]))
        # print(gt_read(house_gt[0]))
        #
        # box1 = pred_read(house_pred[0])
        # box1 = (box1[2], box1[3], box1[2]+box1[4], box1[3]+box1[5])
        # box2 = gt_read(house_gt[0])
        # box2 = (box2[0], box2[1], box2[0]+box2[2], box2[1]+box2[3])

        TP = 0 # 옳은 검출
        FN = 0 # 검출되어야 할 것이 검출되지 않았음
        FP = 0 # 틀린 검출
        TN = 0 # 검출되지 말아야 할 것이 검출되지 않았음
        for i in range(len(house_gt)):
            gt_r = gt_read(house_gt[i])
            pred_r = pred_read(house_pred[i])

            if pred_r == None:
                print(f"{house_pred[i]}는 객체 찾기 실패")
                FN += 1
                continue

            confidence_threshold = 0.5

            if pred_r[1] >= confidence_threshold:
                box1 = (gt_r[1], gt_r[2], gt_r[1] + gt_r[3], gt_r[2] + gt_r[4])
                box2 = (pred_r[2], pred_r[3], pred_r[2]+pred_r[4], pred_r[3]+pred_r[5])

                if gt_r[0] != pred_r[0]:
                    print("객체는 찾았으나 잘못 찾았음")
                    FP += 1
                    continue

                iou = round(IoU(box1, box2), 2)

                if iou >= 0.5:
                    print(f'{house_pred[i]}의 iou는 {iou*100}%')
                    TP +=1
                else:
                    print(f'{house_pred[i]}는 객체는 찾았으나 정확도가 떨어짐. iou는 {iou*100}%')
                    FN += 1
            else: FN += 1

        Precision = round(TP / (TP+FP), 2) # 검출된 애들중에서 맞는애들, 오검출
        Recall = round(TP / (TP+FN), 2) # 맞췄어야하는 애들중에서 참으로 맞춘애들, 미검출
        Accuracy = round((TP+TN)/(TP+TN+FP+FN), 2)
        F1_score = round(2*(Recall*Precision)/(Recall+Precision), 2)
        result_list.append(f'{name} 전제 {len(house_gt)}개에서 TP는 {TP}, FP은 {FP}, FN는 {FN}, 정밀도는 {Precision}, 재현율는 {Recall}, Accuracy는 {Accuracy}, F1_score는 {F1_score}')
    print(result_list)




    # answer이 잘 label 되었는지 확인해 보았습니다
    # with open(f'{gt_path}{house_gt[57]}', 'r') as f:
    #     json_data = json.load(f)
    #
    #
    # f = open(f'{pred_path}{house_pred[0]}', 'r')
    # c = f.readlines()
    # print(c, c[2])
    # a = f.readlines()[1]
    # b = a.split(',')
    # print(a)
    # print(b)
    #
    #
    # img = cv2.imread(f'{gt_path}{house_img[57]}')
    # c_x = int(json_data[0]['annotations'][0]['coordinates']['x'])
    # c_y = int(json_data[0]['annotations'][0]['coordinates']['y'])
    # w = int(json_data[0]['annotations'][0]['coordinates']['width'])
    # h = int(json_data[0]['annotations'][0]['coordinates']['height'])
    # x = c_x - (w//2)
    # y = c_y - (h//2)
    # print(x, y, w, h)
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.imshow('house', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()