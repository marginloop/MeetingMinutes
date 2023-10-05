
from Chat import Chat

class Summarizer():

    @classmethod
    def meeting_minutes(cls, transcription):
        abstract_summary = cls.abstract_summary_extraction(transcription)
        key_points = cls.key_points_extraction(transcription)
        action_items = cls.action_item_extraction(transcription)
        sentiment = cls.sentiment_analysis(transcription)
        return f"abstract_summary: {abstract_summary},/n \
            key_points: {key_points},/n \
            action_items: {action_items},/n \
            sentiment: {sentiment}"

   
    
    @classmethod
    def abstract_summary_extraction(cls, transcription):
        prompt = transcription
        systemPrompt = "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."

        response = Chat.chat(systemPrompt, prompt)
        return response
    
    @classmethod
    def key_points_extraction(cls, transcription):
        prompt = transcription
        systemPrompt = "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about."

        response = Chat.chat(systemPrompt, prompt)
        return response

    @classmethod
    def action_item_extraction(cls, transcription):
        prompt = transcription
        systemPrompt = "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."

        response = Chat.chat(systemPrompt, prompt)
        return response
    
    @classmethod
    def sentiment_analysis(cls, transcription):
        prompt = transcription
        systemPrompt = "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible."

        response = Chat.chat(systemPrompt, prompt)
        return response