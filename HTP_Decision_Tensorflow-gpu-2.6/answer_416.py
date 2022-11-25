import cv2
import os

list_name = ['house', 'tree', 'person']
for name in list_name:
    path = f"./data/HTP_paper/{name}/"
    img_list = os.listdir(path)

    for i in range(len(img_list)):
        img = cv2.imread(f"{path}{img_list[i]}")

        img = cv2.resize(img, (416, 416))

        cv2.imwrite(f'./data/HTP_paper/{name}_answer_416/{img_list[i]}', img)