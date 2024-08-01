# get packages
import os
import time
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
    BitsAndBytesConfig,
)
import torch
from huggingface_hub import login

# get huggingface_token from environment variables
"""
you need to generate a Hugging Face token and add it as a environement variable.
Make sure you have permission to access to the reposetory 
of the model you want to deploy.
    """
try:
    huggingface_token = os.environ["HUGGINGFACE_ACCESS_TOKEN"]
except Exception as e:
    raise ("generate and add your Hugging Face token as a environmment variable", e)


def get_quant_model(hf_model_name: str):
    """This function aims to get your model from Hugging Face,
    quantized the model into 4 bit with nf4 method
    and return the llm ready to be call

    Args:
        hf_model_name (str): huggingface id of the model

    Returns:
        llm: llm ready to be call
    """
    # configure the quantization of the llm model
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    # add your huggingface to have access to the model repo
    login(token=huggingface_token)
    # get the tokenizer of the model
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            hf_model_name,
        )
    except Exception as e:
        print(
            """you don't have access to the model you want to reach. 
              please request access by accessing the model page via 
              Hugging Face.
              """,
            e,
        )
    # quantize the model
    start = time.time()
    quant_model = AutoModelForCausalLM.from_pretrained(
        hf_model_name,
        quantization_config=quantization_config,
        device_map="auto",
    )
    end = time.time()
    print(f"quantization ended and took {end - start}s")
    # get the llm
    llm = pipeline(
        "text-generation",
        model=quant_model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        device_map="auto",
        max_new_tokens=1024,
    )
    print("finish to get the llm. let's generate text")

    return llm
