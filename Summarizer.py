
from Chat import Chat

class Summarizer():


    def summarize_transcription(transcription):
        prompt = f"Please identify the main talking points from the following meeting transcription and provide a short summary for each talking point:\n{transcription}"
        response = Chat.chat(prompt)
        return response.choices[0].text