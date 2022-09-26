import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm
import cv2 as cv
np.set_printoptions(threshold=np.inf)  # 배열 전체 출력



# 이미지 출력 예시 ########################################################################################################
image2= cv.imread('sample/center_middle.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow('simply', image2)
# key = cv.waitKey(0)
# if key == 27:  # esc
#     cv.destroyAllWindows()
# print("Size of Img\n", image2.shape)
# print(image2)
# plt.imshow(image2)
# plt.show()


# qucikdraw data #######################################################################################################
image = [[[2, 2, 18, 20, 24, 46, 78, 230, 223, 216, 206, 200], [241, 199, 82, 2, 0, 9, 13, 13, 64, 202, 255, 255]],
         [[125, 120, 113, 105], [13, 15, 41, 93]],
         [[83, 142], [55, 55]],
         [[49, 54, 67, 72, 71, 60, 52, 51, 66], [102, 106, 103, 100, 91, 89, 100, 117, 119]],
         [[74, 74, 77, 82, 90, 93, 105, 113, 119, 124, 130, 140, 140, 134, 130, 130, 135, 145, 155, 156, 159, 165, 173], [103, 126, 116, 112, 112, 124, 110, 106, 129, 130, 129, 117, 103, 104, 112, 129, 133, 132, 111, 128, 111, 106, 106]],
         [[82, 72, 64, 64, 74, 85, 81, 76, 72, 72, 99, 109, 113, 107, 105, 106, 111, 117, 126, 130, 130, 132, 136, 142, 150, 153], [158, 152, 156, 163, 165, 149, 193, 202, 202, 190, 175, 166, 153, 153, 159, 180, 181, 174, 160, 166, 179, 165, 159, 158, 165, 186]],
         [[177, 170, 164, 162, 165, 177, 190, 191, 187, 190, 195, 209, 199, 190, 184, 186, 202], [148, 150, 161, 176, 183, 179, 159, 148, 174, 179, 179, 152, 193, 207, 210, 187, 165]]]
# image = np.reshape(image, (14, -1))
# print(image)
# print(type(image), len(image), image.shape)
# plt.imshow(image, cmap='gray')
# plt.show()

max = 0
index = 0

for i in range(len(image)):
    if len(image[i][0]) > max:
        max = len(image[i][0])
        index = i
# print(max, index)

# array = [np.zeros([len(image), max])]
# a = [np.zeros(1)]

for i in range(len(image)):
    # print(len(image[i][0]))
    if len(image[i][0]) < max:
        while ((len(image[i][0]) == max) == False):
            image[i][0].append(0)
            image[i][1].append(0)
print(image)
print(type(image), len(image))

# print(image[0][0])
# image[0][0].append(0)
# print(image[0][0])

# reduction = np.squeeze(image, axis=1)
image = np.reshape(image, (14, -1))
print(image)
print(type(image), len(image), image.shape)

# array = np.arange(image, np.uint8)
# array = np.reshape(image, (1024, 720))
# im = Image.fromarray(image)
# im.save("hospital.jpeg")

plt.imshow(image, cmap='gray')
plt.show()



# x,y 좌표로 이미지 표현해보기==============================================================================================
x = []
y = []

for i in range(len(image)):
    if i % 2 == 0:
        x.append(image[i])
    else: y.append(image[i])

x = np.reshape(x, (182, -1))
y = np.reshape(y, (182, -1))
# print(x)
# print(y)

array = []
for i in range(len(x)):
    [a], [b] = (x[i], y[i])
    # print([a, b])
    if ([a, b] == [0, 0]) == False:
        array.append([a, b])
print(array)

# plt.scatter(x, y)
# plt.show()
# a = array[:26]
# b = array[26:52]
# c = array[52:78]
# d = array[78:104]
# e = array[104:130]
# f = array[130:156]
# g = array[156:]
a = array[:12]
b = array[12:16]
c = array[16:18]
d = array[18:27]
e = array[27:50]
f = array[50:76]
g = array[76:]
array = [a] + [b] + [c] + [d] + [e] + [f] + [g]
print(array)
# plt.imshow(array, cmap='gray')
# plt.show()

# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# print(len(e))
# print(len(f))
# print(len(g))

plt.plot(array[0], color="green")
plt.plot(array[1], color="green")
plt.plot(array[2], color="green")
plt.plot(array[3], color="green")
plt.plot(array[4], color="green")
plt.plot(array[5], color="green")
plt.plot(array[6], color="green")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Plot with 2 arbitrary Lines")
plt.show()