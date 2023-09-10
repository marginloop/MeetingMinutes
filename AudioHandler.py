from pydub import AudioSegment

class AudioHandler():

    def split_and_save_audio_chunks(audio_path, chunk_length=10*60*1000):  # Default to 10 minutes
        audio = AudioSegment.from_file(audio_path, format="mp3")
        length_audio = len(audio)
        num_chunks = length_audio // chunk_length + 1

        audio_chunks = [audio[i:i+chunk_length] for i in range(0, length_audio, chunk_length)]
        
        chunk_files = []
        for i, chunk in enumerate(audio_chunks):
            chunk_filename = f"chunk_{i}.mp3"
            chunk.export(chunk_filename, format="mp3")
            chunk_files.append(chunk_filename)

        return chunk_files



