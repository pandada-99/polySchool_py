# 220503 딥러닝수학(신교수님)

from file_read_220503 import read_value

final_points, cnt = read_value("./data/sell_house.txt")
print(cnt)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

#####################머신러닝 방법##########################################################################################
# # weight, bias: 초기값은 랜덤 값으로 셋팅이됨
# # print(model(), parameters): Random 값이 들어 가있음
# # lteration or epoch을 돌면서 model parameter의 값들을 update
# # 실행시마다 결과값이 다른것을 방지하기 위해서
# torch.manual_seed(1)
#
# # train data를 일단 가지고오고,
# # train data로 부터 x, y를 구분해야 함
# # x = [mid, final, report], y = [final points]
# x_train = np.array(final_points)
# y_train = np.array(final_points)
# # print(x_train)
# # x_train, y_train: 2차원 배열
# # pytorch의 입력은 Tensor
# x_train = x_train[:-5, 1:-1] # train_data[:-5, :-1]
# y_train = y_train[:-5, -1] # train_data[:-5, -1]
# x_train = torch.FloatTensor(x_train)
# y_train = torch.FloatTensor(y_train)
#
# # 모델 선언, 가중치 초기화
# # nn.Linear(input Dimension, output Dimension)
# model = nn.Linear(11, 1)
# # optimizer 셋팅
# optimizer = optim.Adam(model.parameters(), lr=0.001)
# # SGD 혹은 Adam 등등 여러개 사용가능
# # lr은 적절한 값을 넣어가며 찾아야함
#
# # Training
# nb_epochs = 10000
# for epoch in range(nb_epochs + 1):
#   # forwarding (H(x) 계산: wx + b)
#   pred = model(x_train)
#   cost = F.mse_loss(pred, y_train)
#   # loss함수 mse외에 다른것도 사용가능
#   optimizer.zero_grad() # pytorch는 별일 없는 이상 이렇게 적어줘야함
#   cost.backward() # Backward 연산
#   optimizer.step() # Weight, Bias를 update
#
#   if epoch % 10 == 0:
#     print(f'Epoch: {epoch:4d} cost: {cost.item(): 4f}')
#
# # model_params = list(model.parameters())
# # print(model_params[0], model_params[1])
#
# # test dataset 가져오기
# x_test = np.array(final_points)
# x_test = x_test[-5:, 1:-1]
# x_test = torch.FloatTensor(x_test)
#
# pred_y = model(x_test)
# print(pred_y)

#####################Linear Algebra_Proj 방법##########################################################################################
# print(final_points)

A = np.array(final_points)
A = A[:-5, 1:-1]
A = A.reshape(cnt-5, 11) # MxM Matrix 형태로 만들어주기 위해 (20x3) => reshape(행의 개수, 열의 개수)
# print(A)
b = np.array(final_points)
b = b[:-5, -1]
b = b.reshape(cnt-5, 1) # (20x1)

# x_hat, 학습기준으로는 weight 값과 동일
x_hat = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), b)
print(x_hat)

test_A = np.array(final_points)
test_A = test_A[-5:, 1:-1]
pred = np.matmul(test_A, x_hat)
print(pred)