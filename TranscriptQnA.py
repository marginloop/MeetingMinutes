import json

class TranscriptQnA():

    @classmethod
    def load_data_from_json(cls, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @classmethod
    def list_files(cls, data):
        for idx, item in enumerate(data, start=1):
            print(f"{idx}. {item.get('file_name')}")

    @classmethod
    def get_transcript_by_index(cls, data, index):
        if 0 <= index < len(data):
            return data[index].get("transcript")
        return None

    @classmethod
    def get_instruction_by_index(cls, data, index):
        if 0 <= index < len(data):
            return data[index].get("instructions")
        return None

    @classmethod
    def run(cls):
        file_path = 'data/transcription_status.json'  # Replace with your JSON file path
        data = cls.load_data_from_json(file_path)
        cls.list_files(data)

        try:
            selection = int(input("Enter the number of the file you want to select: ")) - 1
            if selection < 0 or selection >= len(data):
                print("Invalid selection. Please enter a valid number.")
                return

            print("Choose what to display:")
            print("1. Transcript")
            print("2. Instructions")
            print("3. Both Transcript and Instructions")

            display_choice = int(input("Enter your choice (1, 2, or 3): "))

            if display_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter a valid number (1, 2, or 3).")
                return

            transcript_text = cls.get_transcript_by_index(data, selection)
            instructions = cls.get_instruction_by_index(data, selection)

            if display_choice == 1 or display_choice == 3:
                if transcript_text is not None:
                    print("\nTranscript:")
                    print(transcript_text)
                else:
                    print("No transcript found for selected file.")

            if display_choice == 2 or display_choice == 3:
                if instructions is not None:
                    print("\nInstructions:")
                    print(instructions)
                else:
                    print("No instructions found for selected file.")

        except ValueError:
            print("Please enter a valid number.")

TranscriptQnA.run()
