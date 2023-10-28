import openai
from util.util import util

class Chat():

    @classmethod
    def chat(cls, system_prompt, prompt):
        openai.api_key = util.read_open_api_key()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response['choices'][0]['message']['content']