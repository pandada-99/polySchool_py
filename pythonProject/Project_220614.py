import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

x_data = [ [1, 2], [2, 3], [3, 1],
           [4, 3], [5, 3], [6, 2] ]
y_data = [ [0], [0], [0], [1], [1], [1] ]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)
"""
nn.Sequential() 사용
nn.Sequential(): nn.Module 층을 차례로 쌓을 수 있도록 하는 것
층을 쌓는 역할, wx + b ==> Sigmoid 여러함수들을 연결시켜주는 역할로 이해해도됨.
"""
model = nn.Sequential(
    nn.Linear(2, 1), # input Dim, Output Dim (2, 1)
    nn.Sigmoid() # 출력은 시그모이드 함수의 결과
)

optimizer = optim.SGD(model.parameters(), lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs):
    hypothesis = model(x_train)
    cost = F.binary_cross_entropy(hypothesis, y_train)
    optimizer.zero_grad()
    cost.backward() # Loss function 미분
    optimizer.step()

    if epoch % 20 == 0:
        predicion = hypothesis >= torch.FloatTensor([0.5])
        # 실제 y_train 값(GT)하고 예측된 값과 비교한 결과를 correct_pred에 저장
        correct_pred = predicion == y_train
        accuracy = correct_pred.sum().item() / len(correct_pred)
        print(f'Epoch {epoch:4d}/{nb_epochs}, cost: {cost.item():6f}, Accuracy: {accuracy * 100: 3.2f}%')
