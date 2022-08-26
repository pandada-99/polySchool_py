# 220530 AI기초프로그래밍(신교수님)
import torch
import numpy as np
import matplotlib.pyplot as plt

########################################################################################################################
# Function name: get_data
# Param in: None # get_data() get_data(param1, param2..) X
# param out: Return [Tran Data: x, t], (input x, GT y)
# Description
"""
학습 데이터를 가지고 오는 함수
np.array를 사용해서 tensor로 변경한 후 return
"""
def get_data():
    train_X = np.array([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.16, 7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
    train_Y = np.array([1.7, 2.76, 2.09, 3.19, 1.164, 1.573, 3.336, 2.596, 2.53, 1.254, 2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])

    x = torch.from_numpy(train_X).float().view(17, 1)
    print(x.shape)
    y = torch.from_numpy(train_Y).float()

    return x, y

########################################################################################################################
# Function name: get_weights
# Param in: None
# param out: random weight and bias values
# Description
"""
- weight, bias는 random normal 한 값으로 셋팅
- randn (random normal 약어): 정규분포를 기준으로 랜덤한 값 생성
- vs. rand: 0~1사이의 랜덤한 값을 반환 (균등하게 나누어서 반환)
- w, b는 항상 미분되어야 하므로[최적값을 찾기 위해 => Loss, Cost, Error 값을 최소화] Requires_grad = True로 세팅
"""
def get_weights():
    w = torch.randn(1)
    w.requires_grad = True
    b = torch.randn(1)
    b.requires_grad = True
    return w, b

########################################################################################################################
# Function name: simple_network (or hypothesis_function)
# Param in: x (Train하기 위한 x(입력) 데이터)
# param out: 가설함수의 출력 값
# Description(함수 설명)
"""

"""
def simple_network(x):
    y_pred = torch.matmul(x, w) + b
    return y_pred

########################################################################################################################
# Function name: loss_fn
# Param in: y, y_pred
# param out: loss == error == cost 값 반환
# Description(함수 설명)
"""
MSE: 간단한 설명
"""
def loss_fn(y, y_pred):
    loss = torch.mean((y_pred - y).pow(2).sum())
    for param in [w, b]:
        if not param.grad in None: param.grad.data.zero_()
    loss.backward() # backward를 호출: MSE의 기울기를 계산
    return loss.data

########################################################################################################################
# Function name: optimize
# Param in: learning_rate
# param out: None
# Description(함수 설명)
"""
w, b를 업데이트 해주는 함수
"""
def optimize(lr):
    w.data = w.data = lr * w.grad.data
    b.data -= lr * b.grad.data

########################################################################################################################
# plot_variable 함수는 스스로 작성해 보세요.
# 뒤에 logistic sigmoid 그래프 그릴때 활용.
# plt.plot(x, y, 'r', linestyle='--')
# plt.plot(x, y, 'ro', linestyle='--')
# plot Document. default of z param: blue, 0

# Function name: plot_variable
# Param in: x, y, z = '', **kwargs
# param out: None
# Description(함수 설명)
"""

"""
def plot_variable(x, y, z = '', **kwargs):
    l = []
    for a in [x, y]:
        l.append(a.data)
    plt.plot(l[0], l[1], z, **kwargs)


########################################################################################################################
if __name__ == '__main__':

    X = [1, 2, 3]
    Y = [1, 2, 3]
    # Loss Function을 간결화 하기 위해서 b term은 제거
    # 그래프를 그리기 위해서 w, cost 값을 넣을 빈 리스트 작성
    w_bal = []
    cost_val = []
    for i in range(-30, 50):
        weight = i * 0.1
        w_bal.append(weight)
        curr_cost = ((Y[0]-weight*X[0])**2) + ((Y[1]-weight*X[1])**2) + ((Y[2]-weight*X[2])**2)/3
        cost_val.append(curr_cost)
    # show the cost_function
    plt.plot(w_bal, cost_val)
    plt.show()

    # 학습하기 위한 함수, linear regression 모델을 만들기 위한 함수 작성
    # 결과를 보기 위한 plot 함수도 작성
    # 다음주에 우리가 만든 함수로 학습 진행해보는 코드 작성할 예정
    # grad_zero 해주는 이유에 대해서 코드로 확인
    w, b = get_weights()

########################################################################################################################
# 220613 AI기초프로그래밍(신교수님)

    # # grad.data.zero_, or optimizer.zero_grad()
    # # pytorch에는 위의 초기화 과정이 필요.
    # w = torch.tensor(2.0, requires_grad=True)
    # nb_epochs = 20
    # for epoch in range(nb_epochs):
    #     w.grad.data.zero_()
    #     z = 2 * w
    #     z.backward() # dz/dw (z함수를 w로 미분): 2
    #     print(f'w의 함수 z를 w로 미분한 값: {w.gard}')

    ####################################################################################################################
    # 작성한 함수를 통해서 linear regression 모델 학습
    # 학습할 Data 확인
    # plot을 통해서 data의 분포를 확인
    train_x, train_y = get_data()
    plot_variable(train_x, train_y, 'ro')
    plt.show()

    ####################################################################################################################
    # get_weights 함수를 작성
    # 함수의 반환 값을 랜덤한 weight, bias 값을 셋팅
    w, b = get_weights()

    lr = 1e-4

    for i in range(500):
        y_pred = simple_network(train_x) # wx + b 가설함수를 수행하는 파트
        loss = loss_fn(train_y, y_pred) # mse(y와 y_pred의 차의 제곱의 합.)
        if i % 50 == 0:
            print(f'loss: {loss}, weights: {w}, Bias: {b}')
        optimize(lr) # w,b를 업데이트하는 파트

    plot_variable(train_x, train_y, 'ro')
    plot_variable(train_x, y_pred, label='Fitted line')
    plt.show()

    # ==> Logistic Regression--->