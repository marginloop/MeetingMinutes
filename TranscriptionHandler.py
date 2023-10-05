import whisper

from Chat import Chat

class TranscriptionHandler():
    @classmethod
    def postprocess_transcription(cls, transcription):
        prompt = transcription
        systemPrompt= "You are a helpful assistant for a company. Your task is to correct any spelling discrepancies in the transcribed text. Add necessary punctuation such as periods, commas, and capitalization, and use only the context provided. See the following Transcription"
        
        response = Chat.chat(systemPrompt, prompt)
        return response


    @classmethod
    def transcribe_audio(cls, chunk_file):

        model = whisper.load_model("base")
        result = model.transcribe(chunk_file, fp16=False)  # Pass the audio data array to transcribe
        return result["text"]

