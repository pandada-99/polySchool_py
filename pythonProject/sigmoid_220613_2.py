# 220613 AI기초프로그래밍(신교수님)
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

# 시그모이드 함수 작성
# sigmoid = 1/(1+e^-(Wx+b))
# sigmoid = 1/(1+e^-(x))
def sigmoid(x):
    return 1/(1+np.exp(-x))


def cost_function(hx, y):
    return -((y * torch.log(hx)) + ((1-y) * torch.log(1-hx))).mean()


########################################################################################################################
# Data Prepare
x_data = [ [1, 2], [2, 3], [3, 1],
           [4, 3], [5, 3], [6, 2] ]
y_data = [ [0], [0], [0], [1], [1], [1] ]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# w, b의 데이터를 지정
# x_train: 6x2 * 2x1(weights) ==> 6x1 + b (bias: 1)
# sigmoid(wx+b) ==> if w==0 and b==0 ==> sigmoid(0) ==> 0.5
w = torch.zeros((2, 1), requires_grad=True) # 0으로 시작해도 되는 이유: sigmoid는 0값이 0.5니까!!!
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

print(w, b)

# model parameter를 이용한 inference
# training dataset에 대해서 inference
hypothesis = torch.sigmoid(x_train.matmul(w)+b)
print(hypothesis)

# sigmoid의 출력 값이 0.5 이상이면 1, 아니면 0으로 출력
pred = []
for i in list(hypothesis):
    if i >= 0.5: pred.append(1)
    else: pred.append(0)
print(pred)

prediction = hypothesis >= torch.FloatTensor([0.5])
print(prediction)

########################################################################################################################
# pytorch 기반의 딥러닝 모델을 생성하는 github
# 일반적으로 class를 많이 사용해서 구현이 되어 있음
# class 상속과 관련해서 간단하게 실습
# class명(부모클래스),
# 부모클래스에 있는 거를 그대로 사용하기 위해 super 사용
# 다중상속..

# 상속: 컴퓨터와 노트북
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def browse(self):
        print("web 검색")

# Laptop class는 컴퓨터 클래스를 상속받아 구현
class Laptop(Computer):
    def __init__(self, cpu, ram, battery):
        # 자식클래스에서 부모클래스의 내용을 그대로 사용하고 싶을때.
        # super().부모클래스의 메서드(인자)
        super().__init__(cpu, ram)
        self.battery = battery

    def move(self):
        print("노트북은 이동이 가능함")


# Rectangle 넓이 둘레 계산, square(정사각형) <==rectangle 상속
# cube 정육면체: 상속을 받아서 처리
# 상속에 상속을 간단하게 실습
class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # 넓이 구하는 함수
    def area(self):
        return self.w * self.h

    # 둘레 구하는 함수
    def perimeter(self):
        return (self.w * 2) + (self.h * 2)

class Square:
    def __init__(self, w):
        self.w = w

    # 넓이 구하는 함수
    def area(self):
        return self.w ** 2

    # 둘레 구하는 함수
    def perimeter(self):
        return self.w * 4

class SquareInh(Rect):
    def __init__(self, w):
        super().__init__(w, w)

    def area_tmp(self):
        print("inh: 상속")
        return self.w * self.h

# super() vs super(SquareInh. self)
# 상속 받은 메서드
# 상속에 상속 받은 메서드
class Cube(SquareInh):
    def surface_area(self):
        # SquareInh ==> Rect ==> area_tmp 메서드
        sur_area = super(SquareInh, self).area_tmp()
        # 정육면체의 넓이는 w*h*6
        return sur_area * 6

    def volumn(self):
        vol = super().area_tmp() # SquareInh 클래스의 area_tmp 메서드
        return vol * self.w


if __name__ == "__main__":
    # rect, square class example
    rect = Rect(2, 4)
    print(rect.area(), rect.perimeter())

    squre = Square(4)
    print(squre.area(), squre.perimeter())

    squre_inh = SquareInh(4)
    print(squre_inh.area(), squre_inh.perimeter())

    cube = Cube(3)
    print(cube.surface_area())
    print(cube.volumn())