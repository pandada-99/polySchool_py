from imgaug import augmenters as iaa
import numpy as np
import cv2
import os

list = ['HTP_house', 'HTP_tree', 'HTP_person']

def load_images_from_folder(folder):
    """
    이미지 읽어오는 함수
    :param folder: 이미지 읽어올 폴더 path
    :return: 읽어온 이미지들을 리스트에 넣어서 리턴
    """
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def write_images(folder_name,img_name,images):
    """
    이미지 저장하는 함수
    :param folder_name: 저장할 folder 이름
    :param img_name: 저장할 img 이름
    :param images: 읽어온 이미지 리스트
    :return: 없음
    """
    for i in range(0,len(images)):
        cv2.imwrite('data/%s/mo_%s_%d.jpg'%(folder_name, img_name, i), images[i])
    print("image saving complete")


def image_writer_function(folder, images):
    """
    여러 폴더에 있는 이미지 한번에 저장하기
    :param folder: 저장할 folder 이름
    :param images: 읽어온 이미지 리스트
    :return: 없음
    """
    for i in range(0, len(images)):
        write_images(folder, str(i), images[i])
    print("all images saved to folder")

def augmentations1(images):
    """
    이미지 증강하기
    :param images: 증강시킬 img
    :return: 증강한 img 리스트
    """
    seq1 = iaa.Sequential([
        iaa.AverageBlur(k=(2, 7)),
        iaa.MedianBlur(k=(3, 11))
    ])
    seq2 = iaa.ChannelShuffle(p=1.0)
    seq3 = iaa.Dropout((0.05, 0.1), per_channel=0.5)
    seq4 = iaa.Sequential([
        iaa.Add((-15, 15)),
        iaa.Multiply((0.3, 1.5))
    ])
    print("image augmentation beginning")
    img1 = seq1.augment_images(images)
    print("sequence 1 completed......")
    img2 = seq2.augment_images(images)
    print("sequence 2 completed......")
    img3 = seq3.augment_images(images)
    print("sequence 3 completed......")
    img4 = seq4.augment_images(images)
    print("sequence 4 completed......")
    print("proceed to next augmentations")
    list = [img1, img2, img3, img4]
    return list


if __name__ == '__main__':
    photos = '/data/aug'  # 이미지 읽어올 경로
    folders = os.listdir(photos)
    photos1 = load_images_from_folder(os.path.join(photos, folders[0]))
    photos2 = load_images_from_folder(os.path.join(photos, folders[1]))
    photos3 = load_images_from_folder(os.path.join(photos, folders[2]))

    photo_augmented1234 = augmentations1(photos1)  # 이미지 증강 0,1,2,3 이 리스트 형태로 있다
    image_writer_function('저장할 폴더 이름', '각 이미지에 붙일 이름', photos_augmented1234[0])