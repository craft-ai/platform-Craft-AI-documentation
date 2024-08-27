import time
from src import PREPROMPT
from src.deploy_llm_easy import get_quant_model

# get the huggingface id of the model
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
# get the llm quantized ready to be called
llm = get_quant_model(model_name)


def deploy_llama_easy(message: str):
    """This function aims to generate text with llama3 8B
    from a query
    Args :
        message (str) : the query
    Returns:
        dict: result from text generation
    """

    # formatting the input
    message = [
        {
            "role": "system",
            "content": PREPROMPT,
        },
        {"role": "user", "content": message},
    ]
    # generate text from llm
    start = time.time()

    output = llm(
        message,
        top_k=10,
        max_new_tokens=1024,
        do_sample=True,
    )
    end = time.time()
    print(f"generation ended and took {end - start}s")
    generated_text = output[0]["generated_text"][-1]
    results = generated_text["content"].replace("\n", "")
    return {"results": results}
