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

def run_chat_bot():
    print("IMPORTANT: To exit the program type 'EXIT'.")
    print("Hello! I am Voice Bot! How can I help you today?")
    user_input = input("User: ")
    while(user_input != "EXIT"):
        chat_bot_output = chat_bot_query(user_input)
        print("Voice Bot: " + str(chat_bot_output))

        tts_handling.create_text_to_speech_file(chat_bot_output, client, "speech.mp3")
        tts_handling.play_text_to_speech_file("speech.mp3")
        user_input = input("User: ")

    print("Program Finished.")


# main
run_chat_bot()



