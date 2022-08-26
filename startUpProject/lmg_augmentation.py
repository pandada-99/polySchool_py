import time
import os
from PIL import Image
import sys

print("Process Start.")

start_time = time.time()

file_list = os.listdir('Tyrenol')

file_num = 0

for i in file_list:
    # 부풀릴 이미지 입력
    image_filename = i

    # 결과 저장 폴더 생성
    out_dir = "augmentation"
    if out_dir not in os.listdir():
        os.mkdir(out_dir)

    # 부풀릴 이미지 파일 불러오기
    image = Image.open('C:/Users/AI-00/PycharmProjects/startUpProject/Tyrenol/' + image_filename)
    Xdim, Ydim = image.size

    # 저장된 파일 개수 카운터
    COUNT = 1
    file_num++1

    # 원본 저장
    # 저장할 파일의 이름을 입력합니다.
    temp_new_file_name = "%05d.png" % COUNT
    # 카운트를 1 증가시킵니다.
    COUNT += 1
    # 원본 이미지를 저장합니다.
    image.save(out_dir + "/" + temp_new_file_name)
    image.close()

    # 출력 파일명을 저장할 리스트를 만듭니다.
    FILELIST = [temp_new_file_name]

    for el in FILELIST:
        for i in range(90, 271, 90):
            if COUNT > 2000:
                break
            # 파일을 불러옵니다.
            image = Image.open(out_dir + "/" + el)
            # 변환된 파일을 저장하기 위해 새로운 이름을 지정합니다.
            new_temp_name = str(file_num) + ("%05d.png" % COUNT)
            # 사진이 한 장 만들어질때마다 count를 1씩 증가시킵니다.
            COUNT += 1
            # 사진을 회전시킵니다.
            image = image.rotate(i+1)
            # 간혹 이미지 크기가 변경된다는 이야기가 있어 resize()를 실행합니다.
            image = image.resize((Xdim, Ydim))
            # 회전 된 이미지를 저장합니다.
            image.save(out_dir + "/" + new_temp_name)
            image.close()

# # 폴더 내의 이미지를 모두 읽어와 좌우대칭을 저장합니다. 2의 1승
# for i in range(len(FILELIST)):
#     # 파일을 불러옵니다.
#     image = Image.open(out_dir + "/" + FILELIST[i])
#     # 변환된 파일을 저장하기 위해 새로운 이름을 지정합니다.
#     new_temp_name = "%05d.png" %COUNT
#     # 사진이 한 장 만들어질때마다 count를 1씩 증가시킵니다.
#     COUNT += 1
#     # 이미지를 좌우 반전합니다.
#     image = image.transpose(Image.FLIP_LEFT_RIGHT)
#     # 좌우 반전된 이미지를 저장합니다.
#     image.save(out_dir + "/" + new_temp_name)
#     image.close()
#     # 출력 파일명을 리스트에 저장합니다.
#     FILELIST.append(new_temp_name)
#
# # 리스트 안의 이미지를 모두 읽어와 상하대칭을 저장합니다. 2의 2승
# for i in range(len(FILELIST)):
#     # 파일을 불러옵니다.
#     image = Image.open(out_dir + "/" + FILELIST[i])
#     # 변환된 파일을 저장하기 위해 새로운 이름을 지정합니다.
#     new_temp_name = "%05d.png" % COUNT
#     # 사진이 한 장 만들어질때마다 count를 1씩 증가시킵니다.
#     COUNT += 1
#     # 이미지를 상하 반전합니다.
#     image = image.transpose(Image.FLIP_TOP_BOTTOM)
#     # 상하 반전된 이미지를 저장합니다.
#     image.save(out_dir + "/" + new_temp_name)
#     image.close()
#     # 출력 파일명을 리스트에 저장합니다.
#     FILELIST.append(new_temp_name)
#
# # 리스트 안의 이미지를 모두 읽어와 흑백버전을 저장합니다. 2의 3승
# for i in range(len(FILELIST)):
#     # 파일을 불러옵니다.
#     image = Image.open(out_dir + "/" + FILELIST[i])
#     # 변환된 파일을 저장하기 위해 새로운 이름을 지정합니다.
#     new_temp_name = "%05d.png" % COUNT
#     # 사진이 한 장 만들어질때마다 count를 1씩 증가시킵니다.
#     COUNT += 1
#     # 이미지를 흑백으로 만듭니다.
#     image = image.convert('1')
#     # 흑백으로 변환된 이미지를 저장합니다.
#     image.save(out_dir + "/" + new_temp_name)
#     image.close()
#     # 출력 파일명을 리스트에 저장합니다.
#     FILELIST.append(new_temp_name)

# 리스트 안의 이미지를 모두 읽어와 1도씩 회전합니다. 2의 3승 * 180
# for el in FILELIST:
#     for i in range(90, 271, 90):
#         # 깔끔하게 1,000장만 만듭시다.
#         # 결과물이 1000개를 넘어서면 코드를 종료합니다.
#         if COUNT > 1000:
#             break
#         # 파일을 불러옵니다.
#         image = Image.open(out_dir + "/" + el)
#         # 변환된 파일을 저장하기 위해 새로운 이름을 지정합니다.
#         new_temp_name = "%05d.png" % COUNT
#         # 사진이 한 장 만들어질때마다 count를 1씩 증가시킵니다.
#         COUNT += 1
#         # 사진을 회전시킵니다.
#         image = image.rotate(i+1)
#         # 간혹 이미지 크기가 변경된다는 이야기가 있어 resize()를 실행합니다.
#         image = image.resize((Xdim, Ydim))
#         # 회전 된 이미지를 저장합니다.
#         image.save(out_dir + "/" + new_temp_name)
#         image.close()

print("Process Done.")

end_time = time.time()