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
    return message

