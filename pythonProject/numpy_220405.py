import numpy as np
from matplotlib import pyplot as plt

def showGraph(function, arg):
    x = arg
    y = function(x)
    plt.plot(x, y)
    plt.show()

if __name__== '__main__':
    a = np.array([1, 2, 3, 4])
    print(a)
    b = np.arange(10)
    print(b)
    c = np.linspace(-3.14, 3.14, 10)
    print(c)

    showGraph(np.cos, c)