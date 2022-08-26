# 220613 AI기초프로그래밍(신교수님)
import numpy as np # sigmoid 함수에서 exponetial
import matplotlib.pyplot as plt
from Project_Pytorch_220530 import plot_variable

# 1. Project_Pytorch_220530.py 파일에 plot_variable() 함수를 import
# 2. cost, sigmoid, paper의 수식들을 보고 코드화 할 수 있어야 함.

# 시그모이드 함수 작성
# sigmoid = 1/(1+e^-(Wx+b))
# sigmoid = 1/(1+e^-(x))
def sigmoid(x):
    return 1/(1+np.exp(-x))


########################################################################################################################
if __name__ == "__main__":
    # sigmoid(in_param): -5~5
    x = np.array(-5.0, 5.0, 0.1)
    y = sigmoid(x)