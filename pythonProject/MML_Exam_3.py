import numpy as np

def sigmoid(val):
    return 1 / (1 + np.exp(-val))

lr = 0.5

x1, x2 = 0.1, 0.2
w1 = 0.2
w2 = 0.23
w3 = 0.38
w4 = 0.35
w5 = 0.42
w6 = 0.32
w7 = 0.64
w8 = 0.6
target_o1 = 0.4
target_o2 = 0.6

z1 = w1*x1 + w2*x2
z2 = w3*x1 + w4*x2

h1 = sigmoid(z1)
h2 = sigmoid(z2)

z3 = w5*h1 + w6*h2
dz3_w5 = h1
dz3_w6 = h2
z4 = w7*h1 + w8*h2
dz4_w7 = h1
dz4_w8 = h2
o1 = sigmoid(z3)
o2 = sigmoid(z4)

Eo1 = 0.5*(target_o1 - o1)**2
Eo2 = 0.5*(target_o2 - o2)**2
Etotal = Eo1 + Eo2

print(z1, z2, h1, h2, z3, z4, o1, o2, Etotal)

def backpropagation_1(weight, d_weight, target, output):
    o1_e = -(target - output)
    o1_z3 = output*(1-output)
    z3_w5 = d_weight
    e_w = o1_e*o1_z3*z3_w5
    return weight-lr*(e_w)

if __name__ == '__main__':
    print(backpropagation_1(w5, dz3_w5, target_o1, o1))
    print(backpropagation_1(w6, dz3_w6, target_o1, o1))
    print(backpropagation_1(w7, dz4_w7, target_o2, o2))
    print(backpropagation_1(w8, dz4_w8, target_o2, o2))