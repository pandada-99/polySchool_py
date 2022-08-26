import numpy as np

np.random.seed(8)

def gen_data(mat, n, m):
    for i in range(n):
        for j in range(m):
            mat[i, j] = np.random.randint(0, 10)

def matmul(mat1, mat2, result):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1[0])):
                result[i][j] += mat1[i][k] * mat2[k][j]


if __name__ == '__main__':
    n = np.random.randint(3, 20)
    m = np.random.randint(3, 20)

    print(n, m)

    mat1 = np.zeros((n, m))
    mat2 = np.zeros((m, n))
    result = np.zeros((n, n))
    gen_data(mat1, n, m)
    gen_data(mat2, m, n)

    matmul(mat1, mat2, result)

    print(result, result.shape)