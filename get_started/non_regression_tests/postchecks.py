import time
import dotenv
import os
from craft_ai_sdk import CraftAiSdk

dotenv.load_dotenv()

CRAFT_AI_SDK_TOKEN = os.environ['CRAFT_AI_SDK_TOKEN']
CRAFT_AI_ENVIRONMENT_URL = os.environ['CRAFT_AI_ENVIRONMENT_URL']

# We will check the existence of the executions and if they are succeeded
pipelines_to_check = ["part-4-iristrain", "part-4-iris-deployment"]

sdk = CraftAiSdk(sdk_token=CRAFT_AI_SDK_TOKEN, environment_url=CRAFT_AI_ENVIRONMENT_URL)

# wait for next periodic execution
time.sleep(360)

# # check if the executions have succeeded or not
for pipeline_name in pipelines_to_check:
    # check if there is one execution at least for all the deployments
    try:
        status = sdk.list_pipeline_executions(pipeline_name=pipeline_name)[-1]["status"]
    except Exception:
        print(f"Tried to retrieve last execution of pipeline {pipeline_name}")
        raise f"Error: There was a problem while retrieving the last execution."

    print(f"Status of the pipeline {pipeline_name} after 360sec: {status}.")
    if status.lower() != "succeeded":
        raise f"The pipeline has failed or is still running. We recommand you to check the logs online."