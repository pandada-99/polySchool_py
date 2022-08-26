import pandas as pd
from sklearn import tree
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('data/iris.csv')

    # print(df.head())
    # print(df.info())

    X = []
    Y = []
    for i in range(len(df)):
        iris = [df.loc[i, 'SepalLengthCm'], df.loc[i, 'SepalWidthCm'], df.loc[i, 'PetalLengthCm'], df.loc[i, 'PetalWidthCm']]
        X.append(iris)
        Y.append(df.loc[i, 'Species'])

    iris_model = tree.DecisionTreeClassifier()
    iris_model = iris_model.fit(X, Y)

    plt.figure(figsize=(15, 10))
    tree.plot_tree(iris_model, fontsize=8, filled=True,
                   class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
                   feature_names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
    plt.show()