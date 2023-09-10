
from datetime import datetime
import os
from AudioHandler import AudioHandler
from Summarizer import Summarizer
from TranscriptionHandler import TranscriptionHandler

def process_audio_file(audio_path):
    chunk_files = AudioHandler.split_and_save_audio_chunks(audio_path)
    
    all_transcriptions = []

    for chunk_file in chunk_files:
        transcription = TranscriptionHandler.transcribe_audio(chunk_file)
        all_transcriptions.append(transcription)

        # Optionally, delete the chunk file if you don't need to keep it
        os.remove(chunk_file)

    # Combine all transcriptions
    full_transcription = " ".join(all_transcriptions)
    date_str = datetime.now().strftime("%Y-%m-%d")
    transcription_file_path = f"{date_str}_transcription.txt"
    with open(transcription_file_path, "w") as file:
        file.write(full_transcription)

    full_transcription = TranscriptionHandler.postprocess_transcription(full_transcription)


    # Summarize the entire transcription
    summary = Summarizer.summarize_transcription(full_transcription)
    summary_file_path = f"{date_str}_full_summary.txt"
    
    # Save the full summary
    with open(summary_file_path, "w") as file:
        file.write(summary)

# Example usage
audio_path = "Audio_08_14_2023_17_27_30.mp3"  # Modify as needed
process_audio_file(audio_path)
