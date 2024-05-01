import os
import requests

# Function to generate audio for each text and voice
def generator_audio(text, voice):
    url = 'https://api.soundoftext.com/sounds'
    data = {
        'engine': 'google',
        'data': {
            'text': text,
            'voice': voice
        }
    }
    response = requests.post(url, json=data)
    return response.json().get('id')

# Function to get audio file location
def get_audio(id):
    url = f'https://api.soundoftext.com/sounds/{id}'
    response = requests.get(url).json().get('location') 
    return response

# Function to download audio file
def download_audio(url, folder, file_name):
    file_name = os.path.join(folder, f'{file_name}.mp3')  # Include folder path
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

if __name__ == '__main__':
    # Read text file with multiple words/phrases
    file_path = 'input_text.txt'  # Update with your file path
    folder_name = 'audio_files'  # Folder name for storing audio files
    os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist

    # Process each line in the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tts_text = line.strip()  # Remove leading/trailing whitespace
            voice = 'ru-RU'  # Update with desired voice
            audio_id = generator_audio(tts_text, voice)
            audio_url = get_audio(audio_id)
            download_audio(audio_url, folder_name, tts_text)

    print("Audio files downloaded successfully.")
