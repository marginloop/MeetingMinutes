import openai
from util.util import util
from util.sumarizer import sumarizer


openai.api_key = util.read_open_api_key()
file_name = "data/Journal.m4a"
audio_file= open(file_name, "rb")

transcript = openai.Audio.translate("whisper-1", audio_file)
postprocessed_transcript = sumarizer.postprocessor(transcript=transcript['text'])
meeting_minutes = sumarizer.meeting_minutes(transcription=postprocessed_transcript)

util.transcription_status(file_name, "processed", transcript, meeting_minutes)




