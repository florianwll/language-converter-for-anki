import requests
#author: https://github.com/WadRex 

# {
#     "engine": "google",
#     "data": {
#         "text": "Hello, world",
#         "voice": "en-US"
#     }
# }


# An HTTP status code of 200 with payload:

# {
#     "success": true,
#     "id": "<RFC4122 uuid>"
# }


# https://soundoftext.com/

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

def get_audio(id):
    url = f'https://api.soundoftext.com/sounds/{id}'
    response = requests.get(url).json().get('location') # https://files.soundoftext.com/335668c0-4e29-11ed-a44a-8501b7b1aefa.mp3
    return response

def download_audio(url, file_name):
    # append the mp3 to the tts_text
    file_name = f'{file_name}.mp3'

    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)



if __name__ == '__main__':
    tts_text = "Я тебя люблю"
    voice = 'ru-RU'
    id = generator_audio(tts_text, voice)
    url = get_audio(id)
    download_audio(url, tts_text)