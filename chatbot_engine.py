from pathlib import Path
from openai import OpenAI

import tts_handling

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

def run_chatbot(user_input):
    chat_bot_output = chatbot_query(user_input)
        
    tts_handling.create_text_to_speech_file(chat_bot_output, client, "speech.mp3")
    print("Vocal Bot: " + str(chat_bot_output))
    tts_handling.play_text_to_speech_file("speech.mp3")


if __name__ == "__main__":
    run_chatbot("Hello")
