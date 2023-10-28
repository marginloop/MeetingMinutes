from util.Chat import Chat
class sumarizer:

    @classmethod
    def postprocessor(cls, transcript):
        system_prompt = "You are a helpful transcription assistant. Your task is to correct any spelling discrepancies in the transcribed text. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."
        return Chat.chat(system_prompt=system_prompt, transcript=transcript)
    
    @classmethod
    def meeting_minutes(cls, transcription):
        abstract_summary = abstract_summary_extraction(transcription)
        key_points = key_points_extraction(transcription)
        action_items = action_item_extraction(transcription)
        sentiment = sentiment_analysis(transcription)
        return {
            'abstract_summary': abstract_summary,
            'key_points': key_points,
            'action_items': action_items,
            'sentiment': sentiment
        }