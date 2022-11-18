import cv2
import numpy as np

file_name = ['HTP_tree_32_box30', 'HTP_tree_32_box40', 'HTP_tree_32_box50',
            'HTP_tree_32_box60', 'HTP_tree_32_box70', 'HTP_tree_32_box80', 'HTP_tree_32_box90']

for i in range(len(file_name)):
    img = cv2.imread(f"./data/downsize/tree_downsize_bbox/{file_name[i]}.png")
    kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)

    with open(f'./data/downsize/tree_downsize_bbox/{file_name[i]}.txt', "r") as f:
        box = f.read().split()
        x, y, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])

    cv2.rectangle(img, (x, y), (x2, y2), (225, 0, 0), 2)

    cv2.imwrite(f"./data/downsize/box_img/{file_name[i]}.png")
    # cv2.imshow('Object detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 원본 버전
# img = cv2.imread("./data/downsize/tree/HTP_tree_32.png")
# kernel = np.array([[0, -1, 0],
#                     [-1, 5, -1],
#                     [0, -1, 0]])
# img = cv2.filter2D(img, -1, kernel)
#
# with open('./data/downsize/tree/HTP_tree_32.txt', "r") as f:
#     box = f.read().split()
#     print(box)
#     box[1] = float(box[1])
#     box[2] = float(box[2])
#     box[3] = float(box[3])
#     box[4] = float(box[4])
#
#     box[1] = round(box[1], 0)
#     box[2] = round(box[2], 0)
#     box[3] = round(box[3], 0)
#     box[4] = round(box[4], 0)
#
#     print(box)
#     x, y, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#
# cv2.rectangle(img, (x, y), (x2, y2), (225, 0, 0), 2)
#
# cv2.imwrite(f"./data/downsize/box_img/HTP_tree_32.png", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()