from pathlib import Path
import pygame


def create_text_to_speech_file(chat_bot_output, client, file_name):

    speech_file_path = Path(__file__).parent / file_name
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=str(chat_bot_output)
    )

    with open(speech_file_path, "wb") as file:
        file.write(response.content)

def play_text_to_speech_file(file_name):
    
    pygame.init()
    audio_file_path = Path(__file__).parent / file_name

    pygame.mixer.music.load(str(audio_file_path))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()

