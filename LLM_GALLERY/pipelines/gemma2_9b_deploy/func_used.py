import time
from src.deploy_llm_easy import get_quant_model

# get the huggingface id of the model
model_name = "google/gemma-2-9b-it"
# get the llm quantized ready to be called
llm = get_quant_model(model_name)


def deploy_gemma2_easy(message: str) -> dict:
    """This function aims to generate text with gemma2 9B
    from a query
    Args :
        message (str) : the query
    Returns:
        dict: result from text generation
    """

    # generate text from llm
    start = time.time()
    message = [
        {"role": "user", "content": message},
    ]
    output = llm(message)
    print(output)
    end = time.time()
    print(f"generation ended and took {end - start}s")
    results = output[0]["generated_text"][-1]
    print(results)
    results = results["content"].replace("\n", "")
    return {"results": results}
