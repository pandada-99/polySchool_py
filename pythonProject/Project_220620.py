# 220620 AI기초프로그래밍(신교수님)

import torch
import numpy as np
import torch.optim as optim

data = np.loadtxt('data/data-03-diabetes.csv', delimiter=',', dtype=np.float32)

# print(data.shape)

train_x = data[0:739, :8]
train_y = data[0:739, 8:]
test_x = data[739:, :8]
test_y = data[739:, 8:]

print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)

########################################################################################################################
x_train = torch.FloatTensor(train_x)
y_train = torch.FloatTensor(train_y)

# w, b의 데이터를 지정
# x_train: 6x2 * 2x1(weights) ==> 6x1 + b (bias: 1)
# sigmoid(wx+b) ==> if w==0 and b==0 ==> sigmoid(0) ==> 0.5
w = torch.zeros((8, 1), requires_grad=True) # 0으로 시작해도 되는 이유: sigmoid는 0값이 0.5니까!!!
# w = torch.randn((2, 1), requires_grad=True) # 랜덤도 가능
b = torch.zeros(1, requires_grad=True)

optimizer = optim.SGD([w, b], lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs+1):
    # 1. Hypothesis 함수 (Forward)
    # sigmoid function 작성한 것을 import 해서 사용해도 됨.
    # sigmoid = 1/1+e^(-wx+b)
    hx = 1 / (1 + torch.exp(-(x_train.matmul(w) + b)))

    # 2. Cost Function 사용
    # cost(hx) 1: -log(h(x))
    # cost(hx) 0: -log(1-h(x))
    cost = -((y_train * torch.log(hx)) + ((1-y_train) * torch.log(1-hx))).mean()
    # cost = F.binary_cross_entropy(hx, y_train) 와 같은것!!!!
    # cost = cost_function(hx, y_train)

    # 3. 최적화 (loss, cost function을 미분하고, 경사타고 내려오면서 w, b 업데이트)
    optimizer.zero_grad()
    cost.backward() # Loss function 미분
    optimizer.step() # SGD, lr 만큼 내려가면서 w, b 업데이트

    # 4. loss 값 출력
    if epoch % 100 == 0:
        print(f'Epoch {epoch:4d}/{nb_epochs}, cost: {cost.item(): .6f}')

# print(w, b)

# model parameter를 이용한 inference
# training dataset에 대해서 inference
hypothesis = torch.sigmoid(x_train.matmul(w)+b)
# print(hypothesis)

# sigmoid의 출력 값이 0.5 이상이면 1, 아니면 0으로 출력
pred = []
for i in list(hypothesis):
    if i >= 0.5: pred.append(1)
    else: pred.append(0)
print(pred)

########################################################################################################################
# import torch.nn as nn
# import torch.nn.functional as F
#
# model = nn.Sequential(
#     nn.Linear(2, 2), # input Dim, Output Dim (2, 1)
#     nn.Sigmoid() # 출력은 시그모이드 함수의 결과
# )
#
# optimizer = optim.SGD(model.parameters(), lr=1)
#
# nb_epochs = 1000
# for epoch in range(nb_epochs):
#     hypothesis = model(x_train)
#     cost = F.binary_cross_entropy(hypothesis, y_train)
#     optimizer.zero_grad()
#     cost.backward() # Loss function 미분
#     optimizer.step()
#
#     if epoch % 20 == 0:
#         predicion = hypothesis >= torch.FloatTensor([0.5])
#         # 실제 y_train 값(GT)하고 예측된 값과 비교한 결과를 correct_pred에 저장
#         correct_pred = predicion == y_train
#         accuracy = correct_pred.sum().item() / len(correct_pred)
#         print(f'Epoch {epoch:4d}/{nb_epochs}, cost: {cost.item():6f}, Accuracy: {accuracy * 100: 3.2f}%')