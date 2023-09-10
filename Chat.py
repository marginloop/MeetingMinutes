
import openai

class Chat():
    #openai.api_key = "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" # Remember to handle this securely
    openai.api_base = "http://localhost:4891/v1"

    def __init__(self) -> None:
        self.model= "ggml-wizard-13b-uncensored"


    def chat(self, prompt):
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=50,
            temperature=0.28,
            top_p=0.95,
            n=1,
            echo=True,
            stream=False
        )
        return response