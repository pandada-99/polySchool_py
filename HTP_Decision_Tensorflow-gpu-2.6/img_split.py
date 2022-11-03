import os
import shutil
import splitfolders




# 일단 book_KHTP 파일들 이름에 tree, person을 넣어주자
# path = "./data/img_all/tree/"
# file_list = os.listdir(path)
# print(len(file_list))
#
#
# for i in range(len(file_list)):
#     shutil.move(path + file_list[i], path + f"{file_list[i][0:10]}tree_{file_list[i][10:]}")

# path = "./data/img_all/person/"
# file_list = os.listdir(path)
# print(len(file_list))
# 
# 
# for i in range(len(file_list)):
#     shutil.move(path + file_list[i], path + f"{file_list[i][0:10]}person_{file_list[i][10:]}")




# tree랑 person은 라벨을 0으로 바꾼다~~!
# path = "./data/img_all/tree/"
# file_list = os.listdir(path)
# tree_pt = [file for file in file_list if file.endswith(".png")]
# tree_lb = [file for file in file_list if file.endswith(".txt")]
#
# for i in range(len(tree_lb)):
#     f = open(f'./data/img_all/tree/{tree_lb[i]}', 'r')
#     label = f.readline()
#     공백 = label.find(' ')
#     좌표 = label[공백:]
#     new_label = "0" + 좌표
#     print(new_label)
#     print(f'{tree_lb[i]} 완료!')
#     f = open(f'./data/img_all/tree/{tree_lb[i]}', 'w')
#     f.write(new_label)
#
# path = "./data/img_all/person/"
# file_list = os.listdir(path)
# person_pt = [file for file in file_list if file.endswith(".png")]
# person_lb = [file for file in file_list if file.endswith(".txt")]
#
# for i in range(len(person_lb)):
#     f = open(f'./data/img_all/person/{person_lb[i]}', 'r')
#     label = f.readline()
#     공백 = label.find(' ')
#     좌표 = label[공백:]
#     new_label = "0" + 좌표
#     print(new_label)
#     print(f'{person_lb[i]} 완료!')
#     f = open(f'./data/img_all/person/{person_lb[i]}', 'w')
#     f.write(new_label)
# f.close()




# train, validation 으로 나누기
# splitfolders.ratio("./data/img_all/house", output="./data/house_split", seed=1234, ratio=(0.8, 0.2), group_prefix=2)
# splitfolders.ratio("./data/img_all/tree", output="./data/tree_split", seed=1234, ratio=(0.8, 0.2), group_prefix=2)
# splitfolders.ratio("./data/img_all/person", output="./data/person_split", seed=1234, ratio=(0.8, 0.2), group_prefix=2)




# img 파일들의 경로를 텍스트 파일에 추가하기
# name = ['house', 'tree', 'person']
# for i in name:
#     path = f"./data/{i}_split/train/class1"
#     file_list = os.listdir(path)
#     person_pt = [file for file in file_list if file.endswith(".png")]
#
#     f = open(f'./data/{i}_train.txt', 'a')
#     for j in range(len(person_pt)):
#         file_name = person_pt[j]
#         f.write(f'/home/ai22/pythonProject/HTP/data/{i}_split/train/class1/' + str(file_name) + "\n")
#
#
# f.close()