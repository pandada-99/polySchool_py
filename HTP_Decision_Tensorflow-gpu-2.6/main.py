import os
import shutil
import glob
import splitfolders


# ########## 파일 img와 txt로 구분하기 ##########
#
# path_h = 'data/house'
# path_t = 'data/tree'
# path_p = 'data/person'
#
# list_h = os.listdir(path_h)
# list_t = os.listdir(path_t)
# list_p = os.listdir(path_p)
#
#
# for i in range(len(list_p)):
#     if list_p[i][-1] == 'g':
#         shutil.move(path_p + '/' + list_p[i], './data/img' + '/' + list_p[i])
#     elif list_p[i][-1] == 't':
#         shutil.move(path_p + '/' + list_p[i], './data/label' + '/' + list_p[i])
#
# for i in range(len(list_t)):
#     if list_t[i][-1] == 'g':
#         shutil.move(path_t + '/' + list_t[i], './data/img' + '/' + list_t[i])
#     elif list_t[i][-1] == 't':
#         shutil.move(path_t + '/' + list_t[i], './data/label' + '/' + list_t[i])
#
# for i in range(len(list_h)):
#     if list_h[i][-1] == 'g':
#         shutil.move(path_h + '/' + list_h[i], './data/img' + '/' + list_h[i])
#     elif list_h[i][-1] == 't':
#         shutil.move(path_h + '/' + list_h[i], './data/label' + '/' + list_h[i])



# list_label = os.listdir('data/label')
# list_img = os.listdir('data/img')
# list_label = glob.glob("./data/label/*.txt")

# print(len(list_label), len(list_img))

# ########## classes를 1, 2, 3으로 바꾸기 ##########
# for i in range(len(list_label)):
#     if list_label[i][4] == 'h':
#         file_name = list_label[i]
#         f = open(f'./data/label/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "1" + 좌표
#         f = open(f'./data/label/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 't':
#         file_name = list_label[i]
#         f = open(f'./data/label/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "2" + 좌표
#         f = open(f'./data/label/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 'p':
#         file_name = list_label[i]
#         f = open(f'./data/label/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "3" + 좌표
#         f = open(f'./data/label/{file_name}', 'w')
#         f.write(new_label)

# ##### 파일날려먹기전에 test파일로 먼저 시도해보자 #####
# list_test = os.listdir('data/test')
# print(list_test)
# for i in range(len(list_test)):
#     if list_test[i][4] == 'h':
#         file_name = list_test[i]
#         f = open(f'./data/test/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "1" + 좌표
#         print(new_label)
#         f = open(f'./data/test/{file_name}', 'w')
#         f.write(new_label)





########## yolo 학습하기 ##########
# class_count = 0
# test_percentage = 0.1
# paths = []

# ###### class.names 파일 생성하기 ######
# with open('classes.names', 'w') as names, \
#     open('classes.txt', 'r') as txt:
#     for line in txt:
#         names.write(line)
#         class_count +=1
#     print('[classes.names] is created')


# ###### train, validation 으로 나누기 ######
# splitfolders.ratio("./data/img", output="./data/img_split", seed=1234, ratio=(0.9, 0.1))


# ###### img 파일들의 경로를 텍스트 파일에 추가하기 ######
# list_train = os.listdir('./data/img_split/train')
# list_val = os.listdir('./data/img_split/val')
# path_train = '/home/ai22/pythonProject/HTP/data/img_split/train/'
# path_val = './home/ai22/pythonProject/HTP/data/img_split/val/'
# for name in list_train:
#     f = open('./data/img_train.txt', 'a')
#     f.write(path_train + name + "\n")
# for name in list_val:
#     f = open('./data/img_val.txt', 'a')
#     f.write(path_val + name + "\n")


# ###### custom_data.data 파일 생성하기 ######
# train_img_dir = "./data/img_train.txt"
# val_img_dir = "./data/img_val.txt"


# ##### label.txt를 img폴더에 옮기기 ######
# list_train = os.listdir('data/img_split/train')
# list_val = os.listdir('data/img_split/val')
# list_label = os.listdir('data/label')
#
# train_num = len(list_train)
# val_num = len(list_val)
# label_num = len(list_label)
#
# print(train_num, val_num, label_num)
#
# print(list_label[1], list_label[1][:-4])
# print(list_val[1], list_val[1][:-4])

# for i in range(label_num):
#     for j in range(val_num):
#         if list_label[i][:-4] == list_val[j][:-4]:
#             shutil.copy('./data/label/' + list_label[i], './data/img_split/val/' + list_label[i])
#     for j in range(train_num):
#         if list_label[i][:-4] == list_train[j][:-4]:
#             shutil.copy('./data/label/' + list_label[i], './data/img_split/train/' + list_label[i])
#     print(list_label[i] + ' is ok!')


# ########## split된 classes를 0, 1, 2으로 바꾸기 ##########
# list_label = glob.glob("./data/img_split/train/*.txt")
# for i in range(len(list_label)):
#     list_label[i] = list_label[i][23:]
#
# for i in range(len(list_label)):
#     if list_label[i][4] == 'h':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/train/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "0" + 좌표
#         f = open(f'./data/img_split/train/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 't':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/train/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "1" + 좌표
#         f = open(f'./data/img_split/train/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 'p':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/train/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "2" + 좌표
#         f = open(f'./data/img_split/train/{file_name}', 'w')
#         f.write(new_label)
#
# list_label = glob.glob("./data/img_split/val/*.txt")
# for i in range(len(list_label)):
#     list_label[i] = list_label[i][21:]
#
# for i in range(len(list_label)):
#     if list_label[i][4] == 'h':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/val/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "0" + 좌표
#         f = open(f'./data/img_split/val/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 't':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/val/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "1" + 좌표
#         f = open(f'./data/img_split/val/{file_name}', 'w')
#         f.write(new_label)
#     if list_label[i][4] == 'p':
#         file_name = list_label[i]
#         f = open(f'./data/img_split/val/{file_name}', 'r')
#         label = f.readline()
#         공백 = label.find(' ')
#         좌표 = label[공백:]
#         new_label = "2" + 좌표
#         f = open(f'./data/img_split/val/{file_name}', 'w')
#         f.write(new_label)
