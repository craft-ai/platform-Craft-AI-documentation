import time
from src.deploy_llm_easy import get_quant_model
from src import PREPROMPT


# get the huggingface id of the model
model_name = "mistralai/Mistral-7B-Instruct-v0.2"
# get the llm quantized ready to be called
llm = get_quant_model(model_name)


def deploy_mistral_easy(message: str) -> dict:
    """This function aims to generate text with mistral7B V0.2
    from a query
    Args :
        message (str) : the query
    Returns:
        dict: result from text generation
    """

    # formatting the input
    message = f"<s>[INST] {PREPROMPT}\nquestion: {message} [/INST]"
    # generate text from llm
    start = time.time()
    output = llm(
        message,
        top_k=10,
        num_return_sequences=1,
        do_sample=True,
    )
    end = time.time()
    print(f"generation ended and took {end - start}s")
    generated_text = output[0]["generated_text"]
    results = generated_text.split("[/INST]")[1].replace("\n", "")
    return {"results": results}
