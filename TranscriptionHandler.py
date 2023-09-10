import whisper

from Chat import Chat

class TranscriptionHandler():
    @classmethod
    def postprocess_transcription(self, transcription):
        prompt = f"You are a helpful assistant for a company. Your task is to correct any spelling discrepancies in the transcribed text. Add necessary punctuation such as periods, commas, and capitalization, and use only the context provided. See the following Transcription: {transcription}"
        
        response = Chat.chat(prompt)

    @classmethod
    def transcribe_audio(self, chunk_file):
        with open(chunk_file, "rb") as audio_file:
            whisp_model = whisper.load_model("base")
            result = whisp_model.transcribe("audio.mp3")
            return result["text"]

