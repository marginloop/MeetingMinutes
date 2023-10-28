import openai
import json
from util.util import util
from util.Chat import Chat


openai.api_key = util.read_open_api_key()
file_name = "data/Journal.m4a"
audio_file= open(file_name, "rb")

transcript = openai.Audio.translate("whisper-1", audio_file)


util.transcription_status(file_name, "processed", transcript)




