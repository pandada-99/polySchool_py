import cv2
import os

if __name__ == '__main__':
    path_tree = "./data/HTP_paper/person/"
    file_list = os.listdir(path_tree)

    for name in file_list:
        file_name = f'{name}'
        img = cv2.imread(f"./data/HTP_paper/person/{file_name}")

        if img.shape[0] > img.shape[1]:
            img = cv2.resize(img, (595, 842))
        else:
            img = cv2.resize(img, (842, 595))

        cv2.imwrite(f'./data/HTP_paper/person_resize/{file_name}', img)