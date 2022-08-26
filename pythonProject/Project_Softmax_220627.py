# 220627 AI기초프로그래밍(신교수님)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
# pandas ==> get_dummies() ==> Dataframe ==> np.array
import numpy as np


# 8 x 4 (4개 특성(특징)을 가진 데이터: row: 8)
x_train = [[1, 2, 1, 1],
           [2, 1, 3, 2],
           [3, 1, 3, 5],
           [4, 1, 5, 5],
           [1, 7, 5, 5],
           [1, 2, 5, 6],
           [1, 6, 6, 6],
           [1, 7, 7, 7]]
# GT, Label Data, 각 샘플([1, 2, 1, 1] ==> 2)에 대한 GT값
# 0, 1, 2 총 3개의 클래스가 존재
y_train = [2, 2, 2, 1, 1, 1, 0, 0]

# one-hot encoding으로 y-train을 변경
# 1) pandas의 get-dummies() 메서드 사용
# 2) torch: ont_hot() 메서드 존재하지 않습니다. ==>
# 파이토치 시작할때 사용한 scatter, unsqueeze 메서드 등을 이용해서 구현
# 3) check: nn.Linear(), F.CrossEntropy 사용시
# (y_train 자체를 one-hot encoding으로 하지 않아도 자동으로 변환)

df = pd.DataFrame({"y_train": y_train})
print(df.head())
df = pd.get_dummies(df["y_train"])
print(df.head())
# Dataframe ==> array (8x3) => 변환해주어야 학습 가능
new_array = np.array(df)
print(new_array)
# Pytorch에서 사용하기 위해서는 Tensor 변경
y_train_new = torch.FloatTensor(new_array)
print(y_train_new.shape)

x_train = torch.FloatTensor(x_train)
# scatter_ 메서드 사용을 위해 LongTensor로 변경
y_train = torch.LongTensor(y_train)

# scatter, unsqueeze를 이용한 one-hot encoding 구현
# y_one_hot의 사이즈를 정의
# row가 8개 있고, classes가 3개 있으므로 8x3 one-hot encoding된 데이터 필요
y_one_hot = torch.zeros(8, 3)
# y_train.shape ==> (8, ) ==> (8x1)
# squeeze(제거하다) ==> (8x1) ==> (8)
# row(0), col(1) ==> unsqueeze(0) ==> 1x8, unsqueeze(1) ==> 8x1
# scatter: 흩어지다. (열방향 또는 행방향으로 흩어짐)
# scatter: parameter 첫 번째: 어느 dim으로 확장할건지 결정
# scatter: parameter 세 번째: y_train 값에 해당하는 인덱스를 1에 삽입
# _: inplace=True 같은 개념
y_one_hot.scatter_(1, y_train.unsqueeze(1), 1)
# y_one_hot.scatter_(1, y_train.unsqueeze(1), 2)
print(y_one_hot.shape, y_one_hot)

# 학습을 하기 위한 준비
# 1) weight, bias shape 정의
# 2) optimizer를 뭘 쓸지 등을 정의
# 3) for문에서 정의된 epoch 수만큼 돌면서 w, b 값 학습
# 3-1) 가설함수(hypothesis: softmax)
# 3-2) cost function: cross-entropy
"""
x_train shape: 8x4
y_train shape: 8x3
x_train * w ==> y_train
8x4 matrix multiplication 4x3 ==> 8x3
"""
w = torch.zeros((4, 3), requires_grad=True)
b = torch.zeros(3, requires_grad=True)

optimizer = optim.SGD([w, b], lr=0.1)

# z = torch.FloatTensor([1, 2, 3])
# torch.exp(z[0] / (torch.exp(z[0]) + torch.exp(z[1]) + torch.exp(z[2])))
# F.softmax(z)

model = nn.Linear(4, 3) # weight, bias 값 자동으로 생성됨

nb_epochs = 1000
for epoch in range(nb_epochs+1):
    # 1. Hypothesis 함수 (Forward)
    # softmax = exp(wx+b)/ sum(exp(wx+b))
    # ==> F.softmax
    hx = F.softmax(x_train.matmul(w) + b, dim=1)

    # 2. Cost Function 사용
    # cross-entropy: 1/n(y * -log(h(x))) # *: elements-wise 곱
    cost = (y_one_hot * -torch.log(hx)).sum(dim=1).mean()

    # hx와 cost를 간단한 방법으로 학습시키기
    # pred = model(x_train)
    # cost = F.cross_entropy(pred, y_train)

    # 3. 최적화 (loss, cost function을 미분하고, 경사타고 내려오면서 w, b 업데이트)
    optimizer.zero_grad()
    cost.backward()  # Loss function 미분
    optimizer.step()  # SGD, lr 만큼 내려가면서 w, b 업데이트

    # 4. loss 값 출력
    if epoch % 100 == 0:
        print(f'Epoch {epoch:4d}/{nb_epochs}, cost: {cost.item(): .6f}')