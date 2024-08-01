import os
import time
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk.exceptions import SdkException
from craft_ai_sdk.io import Output, OutputDestination, Input, InputSource

# from .step import get_step_description
from dotenv import load_dotenv


""" Running this script will create all the necessary Craft.AI objects to 
deploy a  quantized gemma2 9B on the Craft.AI platform. 
From this, feel free to use the associated endpoint as you wish and make
good use of your LLM! 
"""
load_dotenv(override=True)


def build_gemma2_9b_pipeline_deploy():
    """To deploy gemma2 9B model on the Craft.AI platform,
    make sure you have at least 8Go of VRAM and 22Go of disk available
    on your environement; since:
    - the raw model takes about 18 Go
    - the model quantized into 4 bits takes about 4.5Go
    - the tokenizer takes about 2.5 Go
    """
    # set the name of your deployment
    deployment_name = "llm-gemma2-9b"
    # sdk instantiation

    sdk = CraftAiSdk(
        sdk_token=os.environ.get("CRAFT_AI_SDK_TOKEN"),
        environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    )
    # add your huggingface token into craft platform

    sdk.create_or_update_environment_variable(
        environment_variable_name="HUGGINGFACE_ACCESS_TOKEN",
        environment_variable_value=os.environ["HUGGINGFACE_ACCESS_TOKEN"],
    )
    try:

        print("Deleting deployment...")
        sdk.delete_deployment(deployment_name)
    except SdkException:
        pass
    try:
        print("Deleting pipeline...")
        sdk.delete_pipeline(deployment_name)
    except SdkException:
        pass
    try:
        print("Deleting step...")
        sdk.delete_step(deployment_name)
    except SdkException:
        pass

    # Setting up the necessary configurations for step creation
    container_config = {
        "local_folder": os.environ["LOCAL_DIRECTORY"],
        "language": "python-cuda:3.10-12.1",
        "requirements_path": "requirements.txt",
        "included_folders": ["/"],
    }
    print("Creating step...")

    # Creating the step encapsulating the code deploying gemma2
    sdk.create_step(
        function_path="/pipelines/gemma2_9b_deploy/step.py",
        function_name="deploy_gemma2_easy",
        step_name=deployment_name,
        container_config=container_config,
        outputs=[
            Output(name="results", data_type="json"),
        ],
        inputs=[
            Input(name="message", data_type="string"),
        ],
        timeout_s=7200,
    )

    # Creating the pipeline associated with the step
    print("Creating pipeline...")
    sdk.create_pipeline(
        pipeline_name=deployment_name,
        step_name=deployment_name,
    )

    # Deploying the pipeline using an endpoint
    print("Deploying Pipeline ...")
    ts_start = time.time()
    sdk.create_deployment(
        deployment_name=deployment_name,
        pipeline_name=deployment_name,
        execution_rule="endpoint",
        mode="low_latency",
        inputs_mapping=[
            InputSource(
                step_input_name="message",
                endpoint_input_name="message",
            ),
        ],
        outputs_mapping=[
            OutputDestination(
                step_output_name="results", endpoint_output_name="results"
            ),
        ],
        timeout_s=6000,
    )
    print("deployment has been created")
    update_status = None
    while update_status != "up":
        update_status = sdk.get_deployment(deployment_name)["status"]
        print(
            "waiting endpoint ready...",
            sdk.get_deployment(deployment_name)["status"],
        )
        time.sleep(10)
    sdk.get_deployment(deployment_name)

    ts_stop = time.time()
    duration = ts_stop - ts_start

    print(f"Deployment creation duration: {duration}")
    print("Done!")

    print("Run deployment...")

    sdk.trigger_endpoint(
        deployment_name,
        sdk.get_deployment(deployment_name)["endpoint_token"],
        inputs={
            "message": "Quel est le plus gros animal au monde?",
        },
    )
    print("Deployment is up and run well!!!")


if __name__ == "__main__":
    build_gemma2_9b_pipeline_deploy()
