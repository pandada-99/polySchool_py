import os
import json
import cv2
import matplotlib.pyplot as plt
import numpy as np

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
    confidence_list = []
    F1_score_list = []
    Accuracy_list = []
    for confidence_threshold in range(1, 10):
        list_name = ['house', 'tree', 'person']
        result_list = []
        for name in list_name:
            gt_path = f"./data/HTP_paper/{name}_answer_416/"
            gt_box = os.listdir(gt_path)
            house_gt = [file for file in gt_box if file.endswith(".json")]
            house_img = [file for file in gt_box if file.endswith(".JPG")]

            pred_path = f"./data/HTP_paper/{name}_ver3_416/"
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

                if pred_r[1] >= round(confidence_threshold * 0.1, 1):
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

            if TP == 0:
                Precision = 0
            else: Precision = round(TP / (TP+FP), 2) # 검출된 애들중에서 맞는애들, 오검출
            Recall = round(TP / (TP+FN), 2) # 맞췄어야하는 애들중에서 참으로 맞춘애들, 미검출
            Accuracy = round((TP+TN)/(TP+TN+FP+FN), 2)
            if Precision == 0:
                F1_score = 0
            else: F1_score = round(2*(Recall*Precision)/(Recall+Precision), 2)
            Accuracy_list.append(Accuracy)
            F1_score_list.append(F1_score)
            result_list.append(f'{name} 전제 {len(house_gt)}개에서 TP는 {TP}, FP은 {FP}, FN는 {FN}, 정밀도는 {Precision}, 재현율는 {Recall}, Accuracy는 {Accuracy}, F1_score는 {F1_score}')
        print(result_list)
        confidence_list.append(round(confidence_threshold*0.1, 1))
    print(confidence_list)
    print(Accuracy_list)
    print(F1_score_list)

    Accuracy_mena_list = []
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[:3]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[3:6]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[6:9]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[9:12]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[12:15]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[15:18]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[18:21]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[21:24]), 2))
    Accuracy_mena_list.append(round(np.mean(Accuracy_list[24:]), 2))
    print(Accuracy_mena_list)

    F1_score_mean_list = []
    F1_score_mean_list.append(round(np.mean(F1_score_list[:3]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[3:6]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[6:9]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[9:12]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[12:15]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[15:18]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[18:21]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[21:24]), 2))
    F1_score_mean_list.append(round(np.mean(F1_score_list[24:]), 2))
    print(F1_score_mean_list)

    f, ax = plt.subplots(1, 2, figsize=(12, 8))
    ax[0].plot(confidence_list, Accuracy_mena_list, 'go-')
    ax[0].set_xlabel('confidence threshold')
    ax[0].set_title('Accuracy', fontsize=20)
    ax[0].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    ax[0].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = Accuracy_mena_list[i]
        ax[0].text(confidence_list[i], height - 0.0285, '%.2f' %height, ha='center', va='bottom', size=12)

    ax[1].plot(confidence_list, F1_score_mean_list, 'bo-')
    ax[1].set_xlabel('confidence threshold')
    ax[1].set_title('F1-score', fontsize=20)
    ax[1].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    ax[1].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = F1_score_mean_list[i]
        ax[1].text(confidence_list[i], height - 0.0285, '%.2f' %height, ha='center', va='bottom', size=12)


    house_accuracy = [Accuracy_list[0], Accuracy_list[3], Accuracy_list[6],
                    Accuracy_list[9], Accuracy_list[12], Accuracy_list[15],
                    Accuracy_list[18], Accuracy_list[21], Accuracy_list[24]]
    tree_accuracy = [Accuracy_list[1], Accuracy_list[4], Accuracy_list[7],
                    Accuracy_list[10], Accuracy_list[13], Accuracy_list[16],
                    Accuracy_list[19], Accuracy_list[22], Accuracy_list[25]]
    person_accuracy = [Accuracy_list[2], Accuracy_list[5], Accuracy_list[8],
                    Accuracy_list[11], Accuracy_list[14], Accuracy_list[17],
                    Accuracy_list[20], Accuracy_list[23], Accuracy_list[26]]

    f, bx = plt.subplots(1, 3, figsize=(16, 8))
    bx[0].plot(confidence_list, house_accuracy, 'go-')
    bx[0].set_xlabel('confidence threshold')
    bx[0].set_title('house accuracy', fontsize=20)
    bx[0].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    bx[0].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = house_accuracy[i]
        bx[0].text(confidence_list[i], height - 0.0285, '%.2f' % height, ha='center', va='bottom', size=12)

    bx[1].plot(confidence_list, tree_accuracy, 'bo-')
    bx[1].set_xlabel('confidence threshold')
    bx[1].set_title('tree accuracy', fontsize=20)
    bx[1].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    bx[1].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = tree_accuracy[i]
        bx[1].text(confidence_list[i], height - 0.0355, '%.2f' % height, ha='center', va='bottom', size=12)

    bx[2].plot(confidence_list, person_accuracy, 'ro-')
    bx[2].set_xlabel('confidence threshold')
    bx[2].set_title('person accuracy', fontsize=20)
    bx[2].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    bx[2].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = person_accuracy[i]
        bx[2].text(confidence_list[i], height - 0.0285, '%.2f' % height, ha='center', va='bottom', size=12)


    house_f1 = [F1_score_list[0], F1_score_list[3], F1_score_list[6],
                F1_score_list[9], F1_score_list[12], F1_score_list[15],
                F1_score_list[18], F1_score_list[21], F1_score_list[24]]
    tree_f1 = [F1_score_list[1], F1_score_list[4], F1_score_list[7],
                F1_score_list[10], F1_score_list[13], F1_score_list[16],
                F1_score_list[19], F1_score_list[22], F1_score_list[25]]
    person_f1 = [F1_score_list[2], F1_score_list[5], F1_score_list[8],
                F1_score_list[11], F1_score_list[14], F1_score_list[17],
                F1_score_list[20], F1_score_list[23], F1_score_list[26]]

    f, cx = plt.subplots(1, 3, figsize=(16, 8))
    cx[0].plot(confidence_list, house_f1, 'go-')
    cx[0].set_xlabel('confidence threshold')
    cx[0].set_title('house F1-score', fontsize=20)
    cx[0].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    cx[0].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = house_f1[i]
        cx[0].text(confidence_list[i], height - 0.0285, '%.2f' % height, ha='center', va='bottom', size=12)

    cx[1].plot(confidence_list, tree_f1, 'bo-')
    cx[1].set_xlabel('confidence threshold')
    cx[1].set_title('tree F1-score', fontsize=20)
    cx[1].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    cx[1].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = tree_f1[i]
        cx[1].text(confidence_list[i], height - 0.0355, '%.2f' % height, ha='center', va='bottom', size=12)

    cx[2].plot(confidence_list, person_f1, 'ro-')
    cx[2].set_xlabel('confidence threshold')
    cx[2].set_title('person F1-score', fontsize=20)
    cx[2].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    cx[2].set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = person_f1[i]
        cx[2].text(confidence_list[i], height - 0.0285, '%.2f' % height, ha='center', va='bottom', size=12)

    plt.show()
"""
    plt.figure(figsize=(10, 7))
    plt.subplot(1, 2, 1)
    plt.plot(confidence_list, Accuracy_mena_list, 'go-')
    plt.xlabel('confidence threshold')
    plt.title('Accuracy')
    plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6 ,0.7 ,0.8 ,0.9])
    plt.yticks([0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = Accuracy_mena_list[i]
        plt.text(confidence_list[i], height - 0.25, '%.2f' %height, ha='center', va='bottom', size=12)

    plt.subplot(1, 2, 2)
    plt.plot(confidence_list, F1_score_mean_list, 'bo-')
    plt.xlabel('confidence threshold')
    plt.title('F1_score')
    plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6 ,0.7 ,0.8 ,0.9])
    plt.yticks([0.7, 0.75, 0.8, 0.85, 0.9, 0.95])
    for i in range(len(confidence_list)):
        height = F1_score_mean_list[i]
        plt.text(confidence_list[i], height - 0.25, '%.2f' %height, ha='center', va='bottom', size=12)

    plt.show()
"""
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