from datetime import datetime
import os
#from AudioHandler import AudioHandler
from Summarizer import Summarizer
from TranscriptionHandler import TranscriptionHandler

def process_audio_file(audio_path):

    date_str = datetime.now().strftime("%Y-%m-%d")
    transcription_file_path = f"{date_str}_transcription.txt"

    # Check if the transcription file already exists
    if not os.path.exists(transcription_file_path):
        full_transcription = TranscriptionHandler.transcribe_audio(audio_path)
        with open(transcription_file_path, "w") as file:
            file.write(full_transcription)
    else:
        # If the file exists, read its content into full_transcription
        with open(transcription_file_path, "r") as file:
            full_transcription = file.read()


    summary_file_path = f"{date_str}_full_summary.txt"  
    if not os.path.exists(summary_file_path):
        full_transcription = TranscriptionHandler.postprocess_transcription(full_transcription)

        # Summarize the entire transcription
        summary = Summarizer.meeting_minutes(full_transcription)
        
        
        # Save the full summary
        with open(summary_file_path, "w") as file:
            file.write(summary)
    else:
        # If the file exists, read its content into full_transcription
        with open(summary_file_path, "r") as file:
            full_transcription = file.read()



# Example usage
audio_path = "Audio_08_14_2023_17_27_30.mp3"  # Modify as needed
process_audio_file(audio_path)
