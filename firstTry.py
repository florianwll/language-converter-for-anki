import os
import requests
from bs4 import BeautifulSoup

def convert_text_to_speech(word, lang):
    url = 'https://soundoftext.com/#learn'
    payload = {
        'text': word,
        'lang': lang
    }
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        audio_tag = soup.find('audio')
        if audio_tag and audio_tag.has_attr('src'):
            return audio_tag['src']
        else:
            print("Error: Audio source not found")
    else:
        print("Error:", response.status_code)
    return None

def save_audio_file(audio_url, folder, file_name):
    response = requests.get(audio_url)
    if response.status_code == 200:
        directory = os.path.join(os.getcwd(), folder)
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Audio file saved as {file_path}")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    words = ["привет", "мир", "пример"]  # List of Russian words you want to convert
    chosen_lang = "ru"  # Language code for Russian
    folder_name = "words"  # Folder to save the audio files

    for word in words:
        audio_url = convert_text_to_speech(word, chosen_lang)
        if audio_url:
            file_name = f"{word}.mp3"
            save_audio_file(audio_url, folder_name, file_name)
