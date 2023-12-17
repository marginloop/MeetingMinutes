import json
from util.Chat import Chat

class TranscriptQnA():

    @classmethod
    def load_data_from_json(cls,file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @classmethod
    def list_files(data):
        for idx, item in enumerate(cls,data, start=1):
            print(f"{idx}. {item.get('file_name')}")
        # No need to return anything, just displaying the list
            
    @classmethod
    def get_transcript_by_index(cls,data, index):
        if 0 <= index < len(data):
            return data[index].get("transcript")
        return None
    
    @classmethod
    def get_instruction_by_index(cls,data, index):
        if 0 <= index < len(data):
            return data[index].get("transcript")
        return None
    
    @classmethod
    def get_instructions(cls,transcript):
        system_prompt = "Please review the following meeting transcript and identify any specific instructions, action items, or 'how-to' steps mentioned. Summarize these instructions in a clear and concise manner, listing out any tasks, responsible persons, deadlines, or methods outlined in the discussion."
        return Chat.chat(system_prompt, transcript)
    
    @classmethod
    def run(cls):
        # Example usage
        file_path = 'data/transcription_status.json'  # Replace with your JSON file path
        data = cls.load_data_from_json(file_path)

        # List out files for the user to select
        cls.list_files(data)

        # User selects the file by number
        try:
            selection = int(input("Enter the number of the file you want to select: ")) - 1
            if selection < 0 or selection >= len(data):
                print("Invalid selection. Please enter a valid number.")
            else:
                transcript_text = cls.get_transcript_by_index(data, selection)
                if transcript_text is not None:
                    #print(transcript_text)
                    #print(cls.get_instructions(transcript=transcript_text))
                    print(cls.get_instruction_by_index(data, selection))
                    # Process the transcript text as needed
                else:
                    print(f"No transcript found for selected file.")
        except ValueError:
            print("Please enter a valid number.")


TranscriptQnA.run()