# 220613 AI기초프로그래밍(신교수님)
import torch
import torch.nn as nn
import torch.nn.functional as F

# pytoch에 Datest, DataLoader 라이브러리를 이용해서
# 데이터를 보다 쉽게 load 할 수 있음
# Data Shuffle 기능, Batch 등과 같은 옵션을 지정할 수 있음
# augmentation: Transform 별도의 라이브러리가 존재
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

x_train = torch.FloatTensor([
    [73, 80, 75],
    [90, 82, 77],
    [78, 98, 100],
    [64, 88, 75]
])

y_train = torch.FloatTensor([
    [152],
    [170],
    [182],
    [148]
])

# TensorDataset: 텐서들을 입력받아
# DataLoader의 입력인자인 Dataset 형태로 반환
dataset = TensorDataset(x_train, y_train)
"""
batch_size는 통상적으로 2의 배수를 자주 사용
shuffle=True: Epoch마다 데이터셋을 섞어서 데이터가 학습되는 순서를 변경
==> 모델이 데이터 셋의 순서에 익숙해지는 것을 방지.
"""
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# nn.Linear(input_dim, output_dim)
model = nn.Linear(3, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs):
    for batch_idx, sampels in enumerate(dataloader):
        x_train, y_train = sampels
        # H(x) 계산 (prediction)
        prediction = model(x_train)

        # cost 계산
        cost = F.mse_loss(prediction, y_train)

        # optimization
        optimizer.zero_grad()
        cost.backward()
        optimizer.step()

        print(f'Epoch {epoch:4d}/{nb_epochs},',
              f'Batch {batch_idx+1}/{len(dataloader)},',
              f'Cost: {cost.item():.6f}')
        # cost: Tensor, Tensor의 값을 가지고 오기 위해서. item() 사용