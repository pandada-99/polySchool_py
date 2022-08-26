# 220418 기계학습프로그래밍(강교수님)
def AND_gate(x1, x2, b=1):
    w1 = 0.4
    w2 = 0.2
    w3 = -0.5  # b = - 0.5

    w_sum = (w1 * x1) + (w2 * x2) + (w3 * b)

    # activation function
    # 0 이하는 0, 그 외 1
    if w_sum > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(AND_gate(0, 0))
    print(AND_gate(0, 1))
    print(AND_gate(1, 0))
    print(AND_gate(1, 1))