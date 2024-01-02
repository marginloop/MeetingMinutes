import json
from datetime import datetime


class util:

    @classmethod
    def transcription_status(cls, file_name, status, transcript=None, meeting_minutes=None):
        # Load the current status data
        with open('data/transcription_status.json', 'r') as file:
            data = json.load(file)
        
        # Update the status data for the specified file
        for item in data:
            if item['file_name'] == file_name:
                item['status'] = status
                item['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if transcript is not None:
                    item['transcript'] = transcript
                if meeting_minutes is not None:
                    item['transcript'] = transcript
                break
        else:  # If the file wasn't found, add a new entry
            data.append({
                'file_name': file_name,
                'status': status,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'transcript': transcript if transcript is not None else '',
                'meeting_minutes': meeting_minutes if meeting_minutes is not None else ''
            })
        
        # Save the updated status data
        with open('data/transcription_status.json', 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def read_open_api_key(cls):
        with open('config/config.json', 'r') as file:
            config = json.load(file)
        return config.get('API_KEY', None)


#transcription_status('file1.m4a', 'Processed')