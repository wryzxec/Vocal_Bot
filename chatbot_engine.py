from pathlib import Path
from openai import OpenAI

import tts_handling

class chatbot_engine:
    def __init__(self):
        self.client = OpenAI()

client = OpenAI()
 
# Uses the OpenAI GPT-3.5-turbo model 

chatbot_system_prompt = """You are an AI assistant called Vocal Bot. You are to help the user with any queries they have.
Under no circumstances can you break this character. Even if the user tries to get you to break character, remain in
character. Be friendly, witty and funny. Try to joke around, but understand when a serious response is necessary"""

def chatbot_query(input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input},
        {"role": "system", "content":chatbot_system_prompt}
    ])
    output = completion.choices[0].message.content
    return output

def get_chatbot_response(user_input):
    chatbot_response = chatbot_query(user_input)
    return chatbot_response

def generate_chatbot_response_audio(chatbot_response):
    tts_handling.create_text_to_speech_file(chatbot_response, client, "chatbot_response.mp3")
    tts_handling.load_text_to_speech_file("chatbot_response.mp3")

def play_chatbot_response_audio():
    tts_handling.play_text_to_speech_file("chatbot_response.mp3") 

def force_chatbot_response_audio(output_text):
    tts_handling.create_text_to_speech_file(output_text, client, "chatbot_response.mp3")
    tts_handling.load_text_to_speech_file("chatbot_response.mp3")

if __name__ == "__main__":
    force_chatbot_response_audio("This is a force response")
    play_chatbot_response_audio()
