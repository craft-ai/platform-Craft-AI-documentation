import os
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk.exceptions import SdkException
from dotenv import load_dotenv

load_dotenv()

sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN"),
)

try:
    sdk.delete_pipeline(
        pipeline_name="part-4-iris-deployment",
        force_deployments_deletion=True,
    )
except SdkException as e:
    print(e)

try:
    sdk.delete_pipeline(
        pipeline_name="part-4-iristrain",
        force_deployments_deletion=True,
    )
except SdkException as e:
    print(e)

try:
    sdk.delete_data_store_object("get_started/dataset/iris.parquet")
except SdkException as e:
    print(e)
try:
    sdk.delete_data_store_object("get_started/models/test_model.joblib")
except SdkException as e:
    print(e)
try:
    sdk.delete_data_store_object("get_started/models/test_model_2.joblib")
except SdkException as e:
    print(e)
