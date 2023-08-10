import openai
from datetime import datetime
import os

openai.api_key = "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"

# Function to transcribe audio
def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
        return response['text']


def postprocess_transcription(transcription):
    system_prompt = "You are a helpful assistant for a company. Your task is to correct any spelling discrepancies in the transcribed text. Add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']


# Function to summarize transcription
def summarize_transcription(transcription):
    prompt = f"Please identify the main talking points from the following meeting transcription and provide a short summary for each talking point:\n{transcription}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

# Main function
def process_audio_file(audio_path):
    # Extract the date
    date_str = datetime.now().strftime("%Y-%m-%d")
    transcription_file_path = f"{date_str}_transcription.txt"
    
    # Check if transcription file already exists
    if os.path.exists(transcription_file_path):
        with open(transcription_file_path, "r") as file:
            transcription = file.read()
    else:
        # Transcribe the audio
        transcription = transcribe_audio(audio_path)
        transcription = postprocess_transcription(transcription)
        
        # Save the transcription
        with open(transcription_file_path, "w") as file:
            file.write(transcription)

    # Summarize the transcription
    summary = summarize_transcription(transcription)

    # Save the summary
    summary_file_path = f"{date_str}_summary.txt"
    with open(summary_file_path, "w") as file:
        file.write(summary)


# Example usage
audio_path = "New Recording.m4a"  # Modify as needed
process_audio_file(audio_path)
