from io import BytesIO
from craft_ai_sdk import CraftAiSdk
import joblib
import pandas as pd
from datetime import datetime



def predictIris(input_data: dict, input_model_path:str):

    sdk = CraftAiSdk()
    
    f = BytesIO()
    sdk.download_data_store_object(input_model_path, f)
    model = joblib.load(f)

    input_dataframe = pd.DataFrame.from_dict(input_data, orient="index")
    predictions = model.predict(input_dataframe)

    print(predictions)

    final_predictions = predictions.tolist()

    return {"predictions": final_predictions}
