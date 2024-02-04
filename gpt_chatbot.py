from pathlib import Path
from openai import OpenAI

import tts_handling

client = OpenAI()
 
# Uses the OpenAI GPT-3.5-turbo model 

def chat_bot_query(input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input}
    ])
    output = completion.choices[0].message.content
    return output

user_input = input("User: ")
chat_bot_output = chat_bot_query(user_input)
print("Chatbot: " + str(chat_bot_output))

tts_handling.create_text_to_speech_file(chat_bot_output, client, "speech.mp3")
tts_handling.play_text_to_speech_file("speech.mp3")
