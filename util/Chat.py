import openai

class Chat():

    @classmethod
    def chat(cls, system_prompt, prompt):
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