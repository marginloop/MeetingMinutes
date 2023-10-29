import openai
from pydub import AudioSegment
from util.util import util
from util.sumarizer import sumarizer

def process_audio_chunk(audio_chunk):
    # Save the chunk to a temporary file
    chunk_file_name = "temp_chunk.wav"
    audio_chunk.export(chunk_file_name, format="wav")

    # Process the chunk
    with open(chunk_file_name, "rb") as audio_file:
        transcript = openai.Audio.translate("whisper-1", audio_file)
    return transcript['text']

def main():
    openai.api_key = util.read_open_api_key()
    file_name = "data/WorkMeetingRatingAssignment.m4a"
    
    # Load the audio file
    audio = AudioSegment.from_file(file_name)
    audio = audio.set_frame_rate(16000).set_channels(1)  # Set to mono and 16kHz
    audio.export("converted_file.wav", format="wav")
    
    # Split the audio file into chunks of, for example, 30 seconds each
    chunk_length_ms = 10 * 60 * 1000  # 30 seconds in milliseconds
    audio_chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    
    # Process each chunk and collect the transcripts
    all_transcripts = []
    for idx, audio_chunk in enumerate(audio_chunks):
        print(f"Processing chunk {idx + 1}/{len(audio_chunks)}...")
        transcript = process_audio_chunk(audio_chunk)
        all_transcripts.append(transcript)
    
    # Combine the transcripts from all chunks
    combined_transcript = "\n".join(all_transcripts)
    
    # Generate the meeting minutes from the full transcript
    postprocessed_transcript = sumarizer.postprocessor(transcript=combined_transcript)
    meeting_minutes = sumarizer.meeting_minutes(transcription=postprocessed_transcript)
    
    # Update the status
    util.transcription_status(file_name, "processed", combined_transcript, meeting_minutes)

if __name__ == "__main__":
    main()
