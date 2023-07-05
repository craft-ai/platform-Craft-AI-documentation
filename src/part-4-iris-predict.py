from io import BytesIO
from craft_ai_sdk import CraftAiSdk
import joblib
import pandas as pd
import json
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def predictIris(input_data: dict, input_model: dict):

    model = joblib.load(input_model["path"])

    input_dataframe = pd.DataFrame.from_dict(input_data, orient="index")
    predictions = model.predict(input_dataframe)

    print(predictions)

    return {"predictions": predictions.tolist()}


def trainIris():
    """
    Train Iris function that trains a simple model based on Iris Dataset
    """

    # Init of the sdk
    # because we will use it to communicate with the platform and retrieve a dataset stored on the datastore
    sdk = CraftAiSdk()

    # Download of the iris dataset
    sdk.download_data_store_object(
        object_path_in_datastore="get_started/dataset/iris.parquet",
        filepath_or_buffer="iris.parquet",
    )
    dataset_df = pd.read_parquet("iris.parquet")

    # Creation of the train and test sets
    X = dataset_df.loc[:, dataset_df.columns != "target"].values
    y = dataset_df.loc[:, "target"].values

    np.random.seed(0)
    indices = np.random.permutation(len(X))

    n_train_samples = int(0.8 * len(X))
    train_indices = indices[:n_train_samples]
    val_indices = indices[n_train_samples:]

    X_train = X[train_indices]
    y_train = y[train_indices]
    X_val = X[val_indices]
    y_val = y[val_indices]

    # Init of the model (knn)
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)

    # Metric computation
    mean_accuracy = knn.score(X_val, y_val)
    print("Mean accuracy:", mean_accuracy)

    # Store the trained model on the datastore
    joblib.dump(knn, "iris_knn_model.joblib")

    return {"predictions": {"path": "iris_knn_model.joblib"}}
