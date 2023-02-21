from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def TrainPredictIris():

    iris_X, iris_y = datasets.load_iris(return_X_y=True, as_frame=True)

    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    iris_X_train = iris_X.loc[indices[0:90], :]
    iris_y_train = iris_y.loc[indices[0:90]]
    iris_X_test = iris_X.loc[indices[90:], :]
    iris_y_test = iris_y.loc[indices[90:]]

    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)

    result = knn.predict(iris_X_test)

    print(result)
