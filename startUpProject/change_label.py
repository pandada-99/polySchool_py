import glob

########## split된 classes를 0, 1, 2으로 바꾸기 ##########
list_label = glob.glob("C:/Users/AI-00/Desktop/pancol-A/*.txt")
for i in range(len(list_label)):
    list_label[i] = list_label[i][32:]

for i in range(len(list_label)):
    file_name = list_label[i]
    f = open(f'C:/Users/AI-00/Desktop/pancol-A/{file_name}', 'r')
    label = f.readline()
    공백 = label.find(' ')
    좌표 = label[공백:]
    new_label = "3" + 좌표
    f = open(f'C:/Users/AI-00/Desktop/pancol-A/{file_name}', 'w')
    f.write(new_label)