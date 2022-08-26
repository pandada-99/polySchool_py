# 220516 AI기초프로그래밍(신교수님)
from glob import glob
import numpy as np
from PIL import Image

import torch
# print(torch.__version__)

# 1D ~ ND 까지 실습
# 1D: Vector
# 텐서를 생성: torch.FloatTensor()
# 지난 주의 평균 온도를 백터에 저장
temp = torch.FloatTensor(
    [15, 17.5, 19.2, 22.3, 20.8, 19.1, 16.9]
)
print(temp.size(), temp.dim()) # dim = 차원(dimensional)

# indexing, Slicing: List와 동일한 방법으로
print(f'월, 화의 평균온도는: {temp[0]}, {temp[1]} 입니다.')
print(f'화~목: {temp[1:4]}')
print()

# Matrix: 2 Dimensional Tensor
# 정의: [ [], [] ]
t = torch.FloatTensor(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
)
# t = torch.FloatTensor([ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ])
print(t.size(), t.dim())

# Slicing (Matrix: 행렬(row, column), 첫번째가 row, 두번째가 col)
# 실습
# 첫번째 차원의 모든 것과, 두번째 차원의 두번째 것
print(t[:, 1])
# row의 3번째 요소들과, col의 모든 것
print(t[2, :])
# 4x3 행렬에서 [5, 6], [8, 9] 가지고 오기.
print(t[1:3, 1:3])
print()

# 보스턴 주택 가격 (from sklearn.datasets)
from sklearn.datasets import load_boston
# load_boston 메서드의 반환형이 numpy의 array
boston = load_boston()
# print(boston.data.)
# numpy to pytorch.
boston_tensor = torch.from_numpy(boston.data)
print(boston_tensor.size(), boston_tensor.dim())

# 인덱스 기준으로 1, 11까지의 feature(cols)와 2개의 row를 가지고 오고 싶을때,
# 모든 features와 2개의 row
print(boston_tensor[:2, 1:])
print()


# ======================================================================================================================
# 220523 AI기초프로그래밍(신교수님)

# 3D Tensor
# Color Image: 3D (w, h, channel)
# channel: R, G, B (YUV, LUV)
# 1 channel Image: Garyscale Image(흑백영상)
# batch-size * 1 channel Image ==> 3D
dog = np.array(Image.open("data/dataset_CatDog/training_set/dogs/dog.4.jpg").resize((224, 224)))
# numpy to tensor
dog_tensor = torch.from_numpy(dog)
# 3D Tensor print
print(f'size and dimension of the dog color image: '
      f'{dog_tensor.size()}, {dog_tensor.dim()}')
print()

# 4D Tensor: color images가 여러개 들어가있는 데이터셋 자체가 4D Tensor
data_path = "data/dataset_CatDog/training_set/dogs/"
# 특정 문자를 포함한 모든 것을 가지고 오기 위해서 glob
dogs = glob(data_path + "*.jpg")
# glob 결과는 리스트로 반환
print(dogs[:2])
print()
# 64x224x224x3
img_list = []
for dog in dogs[:64]:
    img_list.append(np.array(Image.open(dog).resize((224, 224))))
print(img_list[0])
dogs_imgs = np.array(img_list) # 최종적으로 np.array로 4D 형식으로
print(dogs_imgs.size, dogs_imgs.shape, dogs_imgs.ndim)
print()
# numpy to tensor
dog_tensor = torch.from_numpy(dogs_imgs)
print(dog_tensor.size(), dog_tensor.dim())
print()


# ======================================================================================================================
# pytorch에서 자주 사용하는 함수
# 내가 사용하지 않더라도 함수가 어떤 의미인지 알고는 있자.
# Broadcasting
# Matrix A, B가 있으면, 덧셈, 뺄셈을 할때는 두 Matrix의 크기가 같아야 함.
# 행렬의 곱: A Matrix의 col 크기와 B Matrix의 row 크기가 같아야 함.
# 파이토치에서는 자동으로 크기를 맞추어서 연산을 수행: 브로드캐스팅 연산
# 1x2 행렬: [ [1, 2] ]: 2D 형태로 표현
m1 = torch.FloatTensor([ [3, 3] ])
m2 = torch.FloatTensor([ [2, 2] ])
print(m1 + m2)

# m1 = 1x2 matrix, m2 = 2x1 matrix
# m1 + m2 ==> broadcasting을 통해서 m1, m2 모두 2x2로 확장해서 계산
m1 = torch.FloatTensor([ [1, 2] ])
m2 = torch.FloatTensor([ [3], [4] ])
print(m1.shape, m2.shape)
print(m1 + m2)
"""
m1 = [
    [1, 2]
    [1, 2]
]
m2 = [
    [3, 3]
    [4, 4]
]
"""
print()

# in-place 연산 (덮어쓰기 여산: pandas)
# in-place: _(언더바) 사용
a = torch.FloatTensor([ [1, 2], [3, 4] ])
# b = torch.FloatTensor([ [1, 2], [3, 4] ])
print(f'{a.add_(2)}\n{a}') # 브로드캐스팅 + in-place 연산 수행
print()

# matrix 곱, elements-wise 곱
# 1) matrix multiplication: tensor.matmul(tensor) (m1.matmul(m2))
# 2) elements-wise 곱: tensor * tensor (m1 * m2, m1.mul(m2))
# m1: 2x2 matrix, m2: 2x1 matrix ==> matmul: 2x1 matrix
m1 = torch.FloatTensor([ [1, 2], [3, 4] ]) # 2x2
m2 = torch.FloatTensor([ [1], [2] ]) # 2x1
print(m1.shape, m2.shape, m1.matmul(m2))
print()

# elements-wise 곱: m1 * m2 크기가 다르기 때문에 수행 불가
# 계산을 하시면 알아서 크기를 맞추어서 계산
"""
[1 2    [1 1
 3 4]    2 2]
"""
print(m1 * m1, m1.mul(m2))
print()

# from torch import cuda
# use_gpu = cuda.is_available()
# print(use_gpu, torch.cuda.device_count())
# a = torch.rand(20000, 20000)
# b = torch.rand(20000, 20000)
# if use_gpu:
#     a = a.cuda()
#     b = b.cuda()
#     a.matmul(b)
# end_time = time.time()


# ======================================================================================================================
# 2) 평균: tensor.mean()
t = torch.FloatTensor([ [1, 2], [3, 4] ])
print(t.mean()) # (1+2+3+4)/4
# torch, dim을 기준으로 연산이 가능
# pandas sum(axis=0): 기본적으로 0: row, 1: column
# "== 연산의 기본이 column 단위로 하는 연산이면: 0: column, 1: row"
# dim 0, 1 이냐에 따라 연산을 할 수 있음
# dim=0 의미: 첫번째 차원을 제거한다는 의미.
# matrix(2D: row, column) 첫번째 차원은 row, 두번째는 col
# row를 배제하고 계산하고 싶을때 (dim=0 옵션 적용)
# 0: column별로 계산, 1: row별로 계산
print(t.mean(dim=0)) # column끼리 계산 (1, 3)의 평균, (2, 4)의 평균
print(t.mean(dim=1)) # row끼리 계산
print(t.sum(dim=0)) # column끼리 계산 (1, 3)의 합, (2, 4)의 합
print(t.sum(dim=1)) # row끼리 계산
print()

# max, argmax
# max: Tensor들의 원소 값 중에 제일 큰 값을 반환
# argmax: Tensor들의 원소 값 중에 제일 큰 값의 "인덱스" 반환
"""
t = [1  2
     3  4]
0:1 / 1:2 / 2:3 / 3:4
"""
print(t.max(), t.argmax())
print()
# 쉬는 시간에 t.max(dim=0), t.argmax(dim=1)
print(t.max(dim=0))
print(t.argmax(dim=1))
print()

# view: 원소의 수(갯수)를 유지하면서 tensor의 shape을 변경
# numpy의 reshape 함수와 동일한 기능
# 텐서의 크기, 차수를 변경하지만 총 원소의 갯수는 변화가 없음
# 2x2x3 tensor 생성
t = torch.FloatTensor(
    [
        [
            [0, 1, 2],
            [3, 4, 5]
        ],
        [
            [6, 7, 8],
            [9, 10, 11]
        ]
    ]
)
print(t.shape, t.dim())

# 3D --> 2D 텐서로 변경
t2 = t.view([-1, 3])
# -1: all(전체를 의미) 2D: row, col
# row: -1 이라는 것은 col 개수에 따라 row의 형태는 알아서 계산해줘
# 12(총 원소의 갯수: 2x2x3) ==> 컬럼을 3으로 고정했음으로 row: 4로 알아서 계산
print(t2, t2.shape)
print()

# 3차원 텐서의 크기만 변경
# 2x2x3 ==> ?x1x3 ==> t.view([-1, 1, 3])
# ? 값은: 4 (2x2x3=12, ?x1x3=12 ==> ?==4)


# ======================================================================================================================
# squeeze <--> unsqueeze
# 2x1 matrix를 원소가 2개인 백터형태로 변경
t = torch.FloatTensor([ [0], [1], [2] ])
t_sq = t.squeeze()
print(t, t_sq, t.shape, t_sq.shape)

t= torch.FloatTensor([0, 1, 2]) # 벡터
t_row = t.unsqueeze(0) # 옵션에 0: row 1추가(1x3)
t_col = t.unsqueeze(1) # 옵션에 1: col에 1추가(3x1)
print(t.shape, t_row.shape, t_col.shape)
print()


# ======================================================================================================================
# concatenate: 두 개의 텐서를 연결해서 하나의 텐서를 생성
# torch.cat 을 사용 (2x2 텐서를 생성하고 연결)
x = torch.FloatTensor([ [1, 2], [3, 4] ])
y = torch.FloatTensor([ [5, 6], [7, 8] ])

t_row = torch.cat([x, y], dim=0)
t_col = torch.cat([x, y], dim=1)
print(t_row, t_row.shape, t_col, t_col.shape)
print()