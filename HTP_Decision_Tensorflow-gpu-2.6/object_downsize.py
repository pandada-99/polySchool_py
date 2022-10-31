import cv2
import numpy as np
import os
from PIL import Image
import random


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
    # 기존 label txt를 0, 1, 2로 바꿔서 저장
    # for i in range(1, 185):
    #     with open("data/HTP_person/HTP_person_" + str(i) + ".txt", "r") as f:
    #         box = f.read().split()
    #     with open("data/downsize/person/HTP_person_" + str(i) + ".txt", "w") as f:
    #         text = box
    #         text[0] = str(2)
    #         text = ' '.join(s for s in text)
    #         f.write(text)

    # 기존 label txt를 bbox형식으로 바꿔서 저장
    # for i in range(1, 91):
    #     img = cv2.imread('data/downsize/tree/HTP_tree_' + str(i) + '.png')
    #     img_w = img.shape[1]
    #     img_h = img.shape[0]
    #
    #     with open("data/HTP_tree/HTP_tree_" + str(i) + ".txt", "r") as f:
    #         box = f.read().split()
    #         box[1], box[2], box[3], box[4] = yolo2bbox(float(box[1]), float(box[2]), float(box[3]), float(box[4]), img_w, img_h)
    #         box[1], box[2], box[3], box[4] = str(box[1]), str(box[2]), str(box[3]), str(box[4])
    #
    #     x, y, w, h = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #     x, y, w, h = int(x), int(y), int(w), int(h)
    #     # cv2.rectangle(img, (x, y), (w, h), (225, 0, 0), 2)
    #     # cv2.imshow('Object detection', img)
    #     # cv2.waitKey(0)
    #     # cv2.destroyAllWindows()
    #
    #     with open("data/downsize/tree/HTP_tree_" + str(i) + ".txt", "w") as f:
    #         text = box
    #         text[0] = str(1)
    #         text = ' '.join(s for s in text)
    #         f.write(text)
    # exit()
    #
    # path = "./data/downsize/tree"
    # file_list = os.listdir(path)
    # tree_pt = [file for file in file_list if file.endswith(".png")]
    # tree_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # # img = cv2.imread(f'./data/downsize/tree/{house_pt[58]}')
    # # with open(f'./data/downsize/tree/{house_lb[58]}', "r") as f:
    # #     box = f.read().split()
    # #     x, y, w, h = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    # #     x, y, w, h = int(x), int(y), int(w), int(h)
    # # cv2.rectangle(img, (x, y), (w, h), (225, 0, 0), 2)
    # # cv2.imshow('Object detection', img)
    # # cv2.waitKey(0)
    # # cv2.destroyAllWindows()
    #
    # img = cv2.imread(f'./data/downsize/tree/{tree_pt[52]}')
    # with open(f'./data/downsize/tree/{tree_lb[52]}', "r") as f:
    #     box = f.read().split()
    #     x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #     x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
    #     print(x, y, x2, y2)
    #
    # img2 = img.copy()
    # img_crop = img[y:y2, x:x2]
    # img_25 = cv2.resize(img_crop, dsize=(0, 0), fx=0.25, fy=0.25)
    # img_50 = cv2.resize(img_crop, dsize=(0, 0), fx=0.5, fy=0.5)
    # img_75 = cv2.resize(img_crop, dsize=(0, 0), fx=0.75, fy=0.75)
    #
    #
    # img_box = np.ones((842, 595, 3), np.uint8) * 255
    # # cv2.imwrite('./data/downsize/tree/box.png', img_box)
    # # cv2.imwrite('./data/downsize/tree_25.png', img_25)
    #
    # # PIL 사용
    # img_box_25 = Image.open("./data/downsize/box.png")
    # img_box_50 = Image.open("./data/downsize/box.png")
    # img_box_75 = Image.open("./data/downsize/box.png")
    # tree25 = Image.open(f"./data/downsize/tree_25.png")
    # tree50 = Image.open(f"./data/downsize/tree_50.png")
    # tree75 = Image.open(f"./data/downsize/tree_75.png")
    # print(tree25.size)
    # print(tree50.size)
    # print(tree75.size)
    #
    # x25 = random.randint(0, 595 - tree25.size[0])
    # y25 = random.randint(0, 842 - tree25.size[1])
    # img_box_25.paste(tree25, (x25, y25))
    # with open("data/downsize/HTP_tree_" + "52" + "_25.txt", "w") as f:
    #     text = ["0", str(x25), str(y25), str(x25+tree25.size[0]), str(y25+tree25.size[1])]
    #     text = ' '.join(s for s in text)
    #     f.write(text)
    #
    # x50 = random.randint(0, 595 - tree50.size[0])
    # y50 = random.randint(0, 842 - tree50.size[1])
    # img_box_50.paste(tree50, (x50, y50))
    #
    # x75 = random.randint(0, 595 - tree75.size[0])
    # y75 = random.randint(0, 842 - tree75.size[1])
    # img_box_75.paste(tree75, (x75, y75))
    #
    # img_box_25.show()
    # img_box_25.save("./data/downsize/box_25.png", 'png')
    # # img_box_50.show()
    # # img_box_50.save("./data/downsize/box_50.png", 'png')
    # # img_box_75.show()
    # # img_box_75.save("./data/downsize/box_75.png", 'png')
    #
    # # 제대로 찾아졌는지 확인
    # # img = cv2.imread('./data/downsize/box_25.png')
    # # cv2.rectangle(img, (x25, y25), (x25+tree25.size[0], y25+tree25.size[1]), (225, 0, 0), 2)
    # # cv2.imshow('Object detection', img)
    #
    # # cv2.rectangle(img, (x, y), (x2, y2), (225, 0, 0), 2)
    # # cv2.imshow('Object detection', img)
    # # cv2.imshow('Object downsize', img_crop)
    # # cv2.imshow('Object 25%', img_25)
    # # cv2.imshow('Object 50%', img_50)
    # # cv2.imshow('Object 75%', img_75)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    ####################### for문으로 자동화(tree) #######################
    # path = "./data/downsize/tree/"
    # file_list = os.listdir(path)
    # tree_pt = [file for file in file_list if file.endswith(".png")]
    # tree_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(tree_pt)):
    #     img = cv2.imread(f'./data/downsize/tree/{tree_pt[i]}')
    #
    #     with open(f'./data/downsize/tree/{tree_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #         x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
    #
    #     # 원본 카피해서 비율별로 자른 애들 만들기
    #     img_cp = img.copy()
    #     img_crop = img_cp[y:y2, x:x2]
    #     for j in range(3, 10):
    #         num = f"0.{j}"
    #         img_down = cv2.resize(img_crop, dsize=(0, 0), fx=float(num), fy=float(num))
    #         cv2.imwrite(f'./data/downsize/tree_{j*10}.png', img_down)
    #
    #         # 빈화면 만들기
    #         img_box = np.ones((842, 595, 3), np.uint8) * 255
    #         cv2.imwrite('./data/downsize/box.png', img_box)
    #
    #         # PIL 사용
    #         img_box = Image.open("./data/downsize/box.png")
    #         tree = Image.open(f"./data/downsize/tree_{j*10}.png")
    #         if ((595 - tree.size[0]) < 1):
    #             x = 0
    #         else: x = random.randint(0, 595 - tree.size[0])
    #         if ((842 - tree.size[1]) < 1):
    #             y = 0
    #         else: y = random.randint(0, 842 - tree.size[1])
    #         img_box.paste(tree, (x, y))
    #         with open(f"data/downsize/tree_downsize/{tree_lb[i][:-4]}_box{j*10}.txt", "w") as f:
    #             text = ["0", str(x), str(y), str(x + tree.size[0]), str(y + tree.size[1])]
    #             text = ' '.join(s for s in text)
    #             f.write(text)
    #         img_box.save(f"./data/downsize/tree_downsize/{tree_pt[i][:-4]}_box{j*10}.png", 'png')
    #         print(f"{tree_pt[i][:-4]}_box{j*10} 완료")

    ####################### for문으로 자동화(person) #######################
    # path = "./data/downsize/person/"
    # file_list = os.listdir(path)
    # person_pt = [file for file in file_list if file.endswith(".png")]
    # person_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(person_pt)):
    #     img = cv2.imread(f'./data/downsize/person/{person_pt[i]}')
    #
    #     with open(f'./data/downsize/person/{person_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #         x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
    #
    #     # 원본 카피해서 비율별로 자른 애들 만들기
    #     img_cp = img.copy()
    #     img_crop = img_cp[y:y2, x:x2]
    #     for j in range(3, 10):
    #         num = f"0.{j}"
    #         img_down = cv2.resize(img_crop, dsize=(0, 0), fx=float(num), fy=float(num))
    #         cv2.imwrite(f'./data/downsize/person_{j*10}.png', img_down)
    #
    #         # 빈화면 만들기
    #         img_box = np.ones((842, 595, 3), np.uint8) * 255
    #         cv2.imwrite('./data/downsize/box.png', img_box)
    #
    #         # PIL 사용
    #         img_box = Image.open("./data/downsize/box.png")
    #         person = Image.open(f"./data/downsize/person_{j*10}.png")
    #         if ((595 - person.size[0]) < 1):
    #             x = 0
    #         else: x = random.randint(0, 595 - person.size[0])
    #         if ((842 - person.size[1]) < 1):
    #             y = 0
    #         else: y = random.randint(0, 842 - person.size[1])
    #         img_box.paste(person, (x, y))
    #         with open(f"data/downsize/person_downsize/{person_lb[i][:-4]}_box{j*10}.txt", "w") as f:
    #             text = ["0", str(x), str(y), str(x + person.size[0]), str(y + person.size[1])]
    #             text = ' '.join(s for s in text)
    #             f.write(text)
    #         img_box.save(f"./data/downsize/person_downsize/{person_pt[i][:-4]}_box{j*10}.png", 'png')
    #         print(f"{person_pt[i][:-4]}_box{j*10} 완료")

    ####################### for문으로 자동화(house) #######################
    # path = "./data/downsize/house/"
    # file_list = os.listdir(path)
    # house_pt = [file for file in file_list if file.endswith(".png")]
    # house_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(house_pt)):
    #     img = cv2.imread(f'./data/downsize/house/{house_pt[i]}')
    #
    #     with open(f'./data/downsize/house/{house_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #         x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
    #
    #     # 원본 카피해서 비율별로 자른 애들 만들기
    #     img_cp = img.copy()
    #     img_crop = img_cp[y:y2, x:x2]
    #     for j in range(3, 10):
    #         num = f"0.{j}"
    #         img_down = cv2.resize(img_crop, dsize=(0, 0), fx=float(num), fy=float(num))
    #         cv2.imwrite(f'./data/downsize/house_{j*10}.png', img_down)
    #
    #         # 빈화면 만들기
    #         img_box = np.ones((595, 842, 3), np.uint8) * 255
    #         cv2.imwrite('./data/downsize/box.png', img_box)
    #
    #         # PIL 사용
    #         img_box = Image.open("./data/downsize/box.png")
    #         house = Image.open(f"./data/downsize/house_{j*10}.png")
    #         if ((842 - house.size[0]) < 1):
    #             x = 0
    #         else: x = random.randint(0, 842 - house.size[0])
    #         if ((595 - house.size[1]) < 1):
    #             y = 0
    #         else: y = random.randint(0, 595 - house.size[1])
    #         img_box.paste(house, (x, y))
    #         with open(f"data/downsize/house_downsize/{house_lb[i][:-4]}_box{j*10}.txt", "w") as f:
    #             text = ["0", str(x), str(y), str(x + house.size[0]), str(y + house.size[1])]
    #             text = ' '.join(s for s in text)
    #             f.write(text)
    #         img_box.save(f"./data/downsize/house_downsize/{house_pt[i][:-4]}_box{j*10}.png", 'png')
    #         print(f"{house_pt[i][:-4]}_box{j*10} 완료")




    # 라벨링 파일이 잘 만들어졌는지 확인해봅시당
    # path = "./data/downsize/house_downsize/"
    # file_list = os.listdir(path)
    # house_pt = [file for file in file_list if file.endswith(".png")]
    # house_lb = [file for file in file_list if file.endswith(".txt")]
    # img = cv2.imread(f'./data/downsize/house_downsize/{house_pt[544]}')
    #
    # with open(f'./data/downsize/house_downsize/{house_lb[544]}', "r") as f:
    #     box = f.read().split()
    #     x, y, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    #
    # cv2.rectangle(img, (x, y), (x2, y2), (225, 0, 0), 2)
    # cv2.imshow('Object detection', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




    # 라벨링 파일을 다시 yolo형식으로 변환해서 저장
    # path = "./data/downsize/house_downsize/"
    # file_list = os.listdir(path)
    # house_pt = [file for file in file_list if file.endswith(".png")]
    # house_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(house_pt)):
    #     print(f'{house_pt[i]} 완료')
    #     img = cv2.imread(f'./data/downsize/house_downsize/{house_pt[i]}')
    #     img_w = img.shape[1]
    #     img_h = img.shape[0]
    #
    #     with open(f'./data/downsize/house_downsize/{house_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #
    #     with open(f'./data/downsize/house_downsize/{house_lb[i]}', "w") as f:
    #         yolo = bbox2yolo(int(box[0]), img_w, img_h, [x, y, x2, y2])
    #         for i in range(len(yolo)):
    #             yolo[i] = str(yolo[i])
    #         yolo = ' '.join(s for s in yolo)
    #         print(yolo)
    #         f.writelines(yolo)

    # path = "./data/downsize/tree_downsize/"
    # file_list = os.listdir(path)
    # tree_pt = [file for file in file_list if file.endswith(".png")]
    # tree_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(tree_pt)):
    #     print(f'{tree_pt[i]} 완료')
    #     img = cv2.imread(f'./data/downsize/tree_downsize/{tree_pt[i]}')
    #     img_w = img.shape[1]
    #     img_h = img.shape[0]
    #
    #     with open(f'./data/downsize/tree_downsize/{tree_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #
    #     with open(f'./data/downsize/tree_downsize/{tree_lb[i]}', "w") as f:
    #         yolo = bbox2yolo(int(box[0]), img_w, img_h, [x, y, x2, y2])
    #         for i in range(len(yolo)):
    #             yolo[i] = str(yolo[i])
    #         yolo = ' '.join(s for s in yolo)
    #         print(yolo)
    #         f.writelines(yolo)

    # path = "./data/downsize/person_downsize/"
    # file_list = os.listdir(path)
    # person_pt = [file for file in file_list if file.endswith(".png")]
    # person_lb = [file for file in file_list if file.endswith(".txt")]
    #
    # for i in range(len(person_pt)):
    #     print(f'{person_pt[i]} 완료')
    #     img = cv2.imread(f'./data/downsize/person_downsize/{person_pt[i]}')
    #     img_w = img.shape[1]
    #     img_h = img.shape[0]
    #
    #     with open(f'./data/downsize/person_downsize/{person_lb[i]}', "r") as f:
    #         box = f.read().split()
    #         x, y, x2, y2 = float(box[1]), float(box[2]), float(box[3]), float(box[4])
    #
    #     with open(f'./data/downsize/person_downsize/{person_lb[i]}', "w") as f:
    #         yolo = bbox2yolo(int(box[0]), img_w, img_h, [x, y, x2, y2])
    #         for i in range(len(yolo)):
    #             yolo[i] = str(yolo[i])
    #         yolo = ' '.join(s for s in yolo)
    #         print(yolo)
    #         f.writelines(yolo)




    # ###### img 파일들의 경로를 텍스트 파일에 추가하기 ######
    # path = "./data/downsize/person_downsize/"
    # file_list = os.listdir(path)
    # person_pt = [file for file in file_list if file.endswith(".png")]
    #
    # f = open('./data/img_train.txt', 'a')
    # for i in range(len(person_pt)):
    #     name = person_pt[i]
    #     f.write(f'/home/ai22/pythonProject/HTP/data/img_split/train/' + str(name) + "\n")

    pass