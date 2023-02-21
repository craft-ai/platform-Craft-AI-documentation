import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def TrainPredictIris(input_data: dict):
    iris_X, iris_y = datasets.load_iris(return_X_y=True, as_frame=True)

    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    iris_X_train = iris_X.loc[indices[0:90], :]
    iris_y_train = iris_y.loc[indices[0:90]]
    # iris_X_test = iris_X.loc[indices[90:], :]
    # iris_y_test = iris_y.loc[indices[90:]]

    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)

    input_dataframe = pd.DataFrame.from_dict(input_data, orient="index")
    result = knn.predict(input_dataframe)

    print(result)

    final_result = result.tolist()
    return {"predictions": final_result}
