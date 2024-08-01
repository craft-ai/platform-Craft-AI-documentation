# Pipeline LLM Gallery

## Description and objective
The Pipeline LLM Gallery is designed for data scientists who wish to rapidly deploy Large Language Models (LLMs) such as Mistral-7B-v0.2, Llama-3-8B, or Gemma-2-9B without the need for extensive coding. This repository provides an easy-to-use framework that streamlines the deployment process, allowing you to focus on leveraging the capabilities of these models for your data science applications.

## Setup
### prerequisites
Before you begin, ensure you have access to the Craft AI platform and that your environment is properly set up. Additionally, make sure that the size of the LLM you want to deploy fits well within the capacity of your environment:


- **Mistral-7B**: your environment should have at least 6Go of VRAM and 18Go of disk available to download, quantize the model and perform the inference.
- **Llama-3-8B**: your environment should have at least 7.5Go of VRAM and 20Go of disk available to download, quantize the model and perform the inference.
- **Gemma-2-9B**: your environment should have at least 8Go of VRAM and 22Go of disk available to download, quantize the model and perform the inference.

### Steps to Get Started

1. *Clone the Repository*: Open your terminal and clone the repository to your local machine. Navigate into the directory **LLM_GALLERY**

2. *Configure Environment Variables*: Create a `.env` file in the root of the project directory. Use the provided `.env_template` as a guideline for filling out the necessary variables. This is crucial for the proper configuration of your deployment environment.

3. *Install the Craft AI SDK*: You need to install the Craft AI SDK to interact with the Craft AI platform. Execute the following command:\
`pip install craft-ai-sdk`\
Make sure that your installed version is equal to or higher than **0.45.0**. You can verify this by checking the installed packages:\
 `pip list | grep craft-ai-sdk`

4. *Choose and Deploy Your LLM Model*: Select the LLM model you wish to deploy. Navigate to the **pipelines** folder and run the script corresponding to your chosen model. For example, to deploy the Mistral model, use the following command:\
`python3 -m LLM_GALLERY.pipelines.mistral_7b_deploy.setup`\
Running this script will create all the necessary Craft.AI objects needed to deploy a quantized Mistral 7B model on the Craft.AI platform.

5. *Use the Endpoint*: After deployment, you will have access to the associated endpoint for your deployed model. You can now utilize this endpoint in your applications and make the most of your LLM.


