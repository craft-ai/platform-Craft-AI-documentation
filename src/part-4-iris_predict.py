from io import BytesIO
import joblib
import pandas as pd
from craft_ai_sdk import CraftAiSdk


def predict(model_path: str, input_data: dict):
    sdk = CraftAiSdk()

    f = BytesIO()
    sdk.download_data_store_object(model_path, f)
    model = joblib.load(f)

    input_dataframe = pd.DataFrame.from_dict(input_data, orient="index")
    output_predictions = model.predict(input_dataframe)

    return {"predictions": output_predictions.tolist()}
