import cv2
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa

def yolo2bbox(x, y, w, h, img_w, img_h):
    """
    labeling yolo format to boundingBox
    :param x: yolo format의 x 중심값
    :param y: yolo format의 y 중심값
    :param w: yolo format의 wide
    :param h: yolo format의 height
    :param img_w: 이미지의 wide
    :param img_h: 이미지의 height
    :return: bbox format의 리스트 반환 (x1, y1, x2, y2)
    """
    x = x * img_w
    y = y * img_h
    w = w * img_w
    h = h * img_h
    x1, y1 = x - w / 2, y - h / 2
    x2, y2 = x + w / 2, y + h / 2
    return [x1, y1, x2, y2]

def bbox2yolo(label, img_w, img_h, box):
    """
    boundingBox를 yolo format으로 복원하기
    :param label: 라벨링 index
    :param img_w: 이미지의 wide
    :param img_h: 이미지의 height
    :param box: bbox format의 리스트
    :return: yolo format의 리스트 반환 (index, x, y, w, h)
    """
    dw = 1./img_w
    dh = 1./img_h
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return [label, x, y, w, h]

if __name__ == '__main__':
    for i in range(1, 185):
        img = cv2.imread('data/HTP_person/HTP_person_' + str(i) + '.png')
        img_w = img.shape[1]
        img_h = img.shape[0]

        with open("data/HTP_person/HTP_person_" + str(i) + ".txt", "r") as f:
            box = f.read().split()
        for j in range(len(box)):
            box[j] = float(box[j])
        # print("원본 yolo", box)

        boxChange = yolo2bbox(box[1], box[2], box[3], box[4], img_w, img_h)
        # print("bbox로 변환", boxChange)
        # img = cv2.rectangle(img, (int(boxChange[0]), int(boxChange[1])), (int(boxChange[2]), int(boxChange[3])), (255, 0, 0), 1)

        input_img = img[np.newaxis, :, :, :]
        bbox = [ia.BoundingBox(x1=boxChange[0], y1=boxChange[1], x2=boxChange[2], y2=boxChange[3])]



        # Img augmetation (축소)
        output_img_s, output_bbox_s = iaa.Affine(scale=0.8)(images=input_img, bounding_boxes=bbox)
        # print("img 축소후 바꾼 bbox", output_bbox_s)

        draw_s = output_bbox_s[0].draw_on_image(output_img_s[0], size=2, color=[0, 0, 255])
        res_s = np.hstack((img, draw_s))
        # cv2.imshow('res_s', res_s)

        boxRestore_s = bbox2yolo(box[0], img_w, img_h, [output_bbox_s[0].x1, output_bbox_s[0].y1, output_bbox_s[0].x2, output_bbox_s[0].y2])
        # print("축소된 img bbox 다시 yolo로 바꿈", boxRestore_s)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_s_" + str(i) + ".png", output_img_s[0])
        with open("data/HTP_person_aug/HTP_person_aug_s_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_s)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (기울기)
        output_img_r, output_bbox_r = iaa.Affine(rotate=-15)(images=input_img, bounding_boxes=bbox)
        # print("img 각도변경(+15)후 바꾼 bbox", output_bbox_r)

        draw_r = output_bbox_r[0].draw_on_image(output_img_r[0], size=2, color=[0, 0, 255])
        res_r = np.hstack((img, draw_r))
        # cv2.imshow('res_r', res_r)

        boxRestore_r = bbox2yolo(box[0], img_w, img_h, [output_bbox_r[0].x1, output_bbox_r[0].y1, output_bbox_r[0].x2, output_bbox_r[0].y2])
        # print("각도변경(+15)된 img bbox 다시 yolo로 바꿈", boxRestore_r)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_r_" + str(i) + ".png", output_img_r[0])
        with open("data/HTP_person_aug/HTP_person_aug_r_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_r)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (기울기2)
        output_img_r2, output_bbox_r2 = iaa.Affine(rotate=15)(images=input_img, bounding_boxes=bbox)
        # print("img 각도변경(-15)후 바꾼 bbox", output_bbox_r2)

        draw_r2 = output_bbox_r2[0].draw_on_image(output_img_r2[0], size=2, color=[0, 0, 255])
        res_r2 = np.hstack((img, draw_r2))
        # cv2.imshow('res_r2', res_r2)

        boxRestore_r2 = bbox2yolo(box[0], img_w, img_h, [output_bbox_r2[0].x1, output_bbox_r2[0].y1, output_bbox_r2[0].x2, output_bbox_r2[0].y2])
        # print("각도변경(-15)된 img bbox 다시 yolo로 바꿈", boxRestore_r2)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_r2_" + str(i) + ".png", output_img_r2[0])
        with open("data/HTP_person_aug/HTP_person_aug_r2_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_r2)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (x이동)
        output_img_x, output_bbox_x = iaa.Affine(translate_px={"x":-40})(images=input_img, bounding_boxes=bbox)
        # print("img 이동(x-40)후 바꾼 bbox", output_bbox_x)

        draw_x = output_bbox_x[0].draw_on_image(output_img_x[0], size=2, color=[0, 0, 255])
        res_x = np.hstack((img, draw_x))
        # cv2.imshow('res_x', res_x)

        boxRestore_x = bbox2yolo(box[0], img_w, img_h, [output_bbox_x[0].x1, output_bbox_x[0].y1, output_bbox_x[0].x2, output_bbox_x[0].y2])
        # print("이동(x-40)된 img bbox 다시 yolo로 바꿈", boxRestore_x)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_x_" + str(i) + ".png", output_img_x[0])
        with open("data/HTP_person_aug/HTP_person_aug_x_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_x)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (x이동2)
        output_img_x2, output_bbox_x2 = iaa.Affine(translate_px={"x":+40})(images=input_img, bounding_boxes=bbox)
        # print("img 이동(x+40)후 바꾼 bbox", output_bbox_x2)

        draw_x2 = output_bbox_x2[0].draw_on_image(output_img_x2[0], size=2, color=[0, 0, 255])
        res_x2 = np.hstack((img, draw_x2))
        # cv2.imshow('res_x2', res_x2)

        boxRestore_x2 = bbox2yolo(box[0], img_w, img_h, [output_bbox_x2[0].x1, output_bbox_x2[0].y1, output_bbox_x2[0].x2, output_bbox_x2[0].y2])
        # print("이동(x+40)된 img bbox 다시 yolo로 바꿈", boxRestore_x2)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_x2_" + str(i) + ".png", output_img_x2[0])
        with open("data/HTP_person_aug/HTP_person_aug_x2_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_x2)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (y이동)
        output_img_y, output_bbox_y = iaa.Affine(translate_px={"y":-40})(images=input_img, bounding_boxes=bbox)
        # print("img 이동(y-40)후 바꾼 bbox", output_bbox_y)

        draw_y = output_bbox_y[0].draw_on_image(output_img_y[0], size=2, color=[0, 0, 255])
        res_y = np.hstack((img, draw_y))
        # cv2.imshow('res_y', res_y)

        boxRestore_y = bbox2yolo(box[0], img_w, img_h, [output_bbox_y[0].x1, output_bbox_y[0].y1, output_bbox_y[0].x2, output_bbox_y[0].y2])
        # print("이동(y-40)된 img bbox 다시 yolo로 바꿈", boxRestore_y)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_y_" + str(i) + ".png", output_img_y[0])
        with open("data/HTP_person_aug/HTP_person_aug_y_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_y)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)



        # Img augmetation (y이동2)
        output_img_y2, output_bbox_y2 = iaa.Affine(translate_px={"y":+40})(images=input_img, bounding_boxes=bbox)
        # print("img 이동(y+40)후 바꾼 bbox", output_bbox_y2)

        draw_y2 = output_bbox_y2[0].draw_on_image(output_img_y2[0], size=2, color=[0, 0, 255])
        res_y2 = np.hstack((img, draw_y2))
        # cv2.imshow('res_y2', res_y2)

        boxRestore_y2 = bbox2yolo(box[0], img_w, img_h, [output_bbox_y2[0].x1, output_bbox_y2[0].y1, output_bbox_y2[0].x2, output_bbox_y2[0].y2])
        # print("이동(y+40)된 img bbox 다시 yolo로 바꿈", boxRestore_y2)

        cv2.imwrite("data/HTP_person_aug/HTP_person_aug_y2_" + str(i) + ".png", output_img_y2[0])
        with open("data/HTP_person_aug/HTP_person_aug_y2_" + str(i) + ".txt", "w") as f:
            text = str(boxRestore_y2)
            text = text.replace(",", "0")
            text = text[1:-1]
            f.writelines(text)


        print(i)











    # cv2.waitKey(0)
    # cv2.destroyAllWindows()