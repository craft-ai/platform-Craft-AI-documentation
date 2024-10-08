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
        pipeline_name="part-1-hello-world",
        force_deployments_deletion=True,
    )
except SdkException as e:
    print(e)
