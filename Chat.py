from gpt4all import GPT4All

class Chat():

    @classmethod
    def segment_text(cls, text, max_tokens=2048, overlap=50):
        words = text.split()
        segments = []
        current_segment = []

        for word in words:
            if len(' '.join(current_segment + [word])) < max_tokens:
                current_segment.append(word)
            else:
                segments.append(' '.join(current_segment))
                current_segment = current_segment[-overlap:] + [word]

        if current_segment:
            segments.append(' '.join(current_segment))

        return segments

    @classmethod
    def chat(cls, systemPrompt, prompt):
        model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

        model.config['systemPrompt'] = systemPrompt

        # If the prompt is short enough, process it directly
        if len(prompt.split()) < 2048:
            return model.generate(prompt, max_tokens=2048)
        
        # Otherwise, segment the prompt and process each segment
        segments = cls.segment_text(prompt)
        responses = [model.generate(segment, max_tokens=2048) for segment in segments]
        
        # Combine the responses
        return ' '.join(responses)
