from pathlib import Path
from openai import OpenAI

import tts_handling

class chatbot_engine:
    def __init__(self):
        self.client = OpenAI()

client = OpenAI()
 
# Uses the OpenAI GPT-3.5-turbo model 

def chatbot_query(input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input}
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

if __name__ == "__main__":
    test_response = get_chatbot_response("Hello")
    print(test_response)
