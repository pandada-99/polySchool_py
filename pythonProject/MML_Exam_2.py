import numpy as np

def inner_product(vectors, in_vec):
    temp = [0, 0]
    for i in range(len(vectors)):
        sum = 0
        for j in range(len(vectors[0])):
            sum += vectors[i][j] * in_vec[j]
            if sum > temp[0]:
                temp[0] = round(sum, 2)
                temp[1] = i
    max = (temp[0], temp[1])
    return max

if __name__ == '__main__':
    np.random.seed(1234)
    doc_vec = np.zeros((100, 6))
    for i in range(len(doc_vec)):
        for j in range(len(doc_vec[0])):
            doc_vec[i][j] = np.random.random()
    print(doc_vec)

    vec_doc1 = [0.2, 0.4, 0.02, 0.1, 0.9, 0.8]

    print(inner_product(doc_vec, vec_doc1))