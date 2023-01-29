import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

def gpt_response(prompt: str, max_tokens: int = 500) -> str:
    """Returns the response from the GPT-3 model.
    :Args:
        - prompt: The prompt to give to the model.
        - max_tokens: The maximum number of tokens to return.
        - temperature: The temperature of the model.
    :Returns:
        - message: The response from the model.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1, # number of responses to generate
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    message = remove_gptresponse_newline(message)
    return message

def remove_gptresponse_newline(message: str) -> str:
    """
    Removes the first part of the gpt response that contains strange text.
    GPT message starts with "*/n/n" (I dont really understand why lol).
    """
    index = message.find("\n\n")
    # 20 is an arbitrary number, but it works for now.
    if index != -1 | index < 20:
        message = message[index + 2 :]

    return message
