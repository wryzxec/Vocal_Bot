import tkinter as tk
import chatbot_engine as chatbot
import tts_handling as tts
import speech_to_text_handling as stt

from PIL import Image, ImageTk
from pathlib import Path

class MyApp:
    def __init__(self, root):
        self.root = root

        SCREEN_WIDTH = self.root.winfo_screenwidth()
        SCREEN_HEIGHT = self.root.winfo_screenheight()

        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.root.state('zoomed')

        self.root.title("Vocal Bot")
        self.root.configure(bg="#1e1e1e")

        self.vocal_bot_title = self.create_vocal_bot_title_label()
        self.vocal_bot_metadata = self.create_vocal_bot_metadata_label()

        self.text_entry = self.create_text_input_box()

        self.speech_input_button = self.create_speech_input_button()
        
        self.speech_listening_label = self.create_speech_listening_label() 
        self.accessibility_label = self.create_accessibility_label()

        self.chatbot_icon_images = {}
        self.chatbot_icon_label = self.create_chatbot_icon("images/chatbot_idle.png")
        
        self.text_entry.bind("<Return>", self.process_input)


    def resize_image(self, image_path, new_width, new_height):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((new_width, new_height))
        return ImageTk.PhotoImage(resized_image)

    def create_text_input_box(self):
        text_entry = tk.Entry(self.root, width=35, font=('Consolas', 25))

        text_entry_x = (self.root.winfo_screenwidth() // 2) - (text_entry.winfo_reqwidth() // 2) - 40
        text_entry_y = (4 / 6) * self.root.winfo_screenheight()

        text_entry.place(x = text_entry_x, y = text_entry_y)
        return text_entry
    
    def create_vocal_bot_title_label(self):
        vocal_bot_title_label = tk.Label(self.root, text="VOCAL BOT", font=('Montserrat', 40, "bold"), bg="#1e1e1e", fg="white")
        vocal_bot_title_label_x = 10
        vocal_bot_title_label_y = 10

        vocal_bot_title_label.place(x=vocal_bot_title_label_x, y=vocal_bot_title_label_y)

        return vocal_bot_title_label
    
    def create_vocal_bot_metadata_label(self):
        vocal_bot_metadata_label = tk.Label(self.root, text="Version: 1.0\nAuthor: Lucas Bruckbauer\nGitHub: wryzxec", justify="left", font=('Consolas', 16), bg="#1e1e1e", fg="grey")
        vocal_bot_metadata_label_x = 10
        vocal_bot_metadata_label_y = self.vocal_bot_title.winfo_reqheight() + 10

        vocal_bot_metadata_label.place(x=vocal_bot_metadata_label_x, y=vocal_bot_metadata_label_y)

        return vocal_bot_metadata_label
    
    def create_accessibility_label(self):
        accessibility_label = tk.Label(self.root, text="Type inside the Text Box or click on the Mic Icon and start speaking", 
                                       font=('Consolas', 16, "bold"), bg="#1e1e1e", fg="grey")
        accessibility_label_x = (self.root.winfo_screenwidth() // 2) - (accessibility_label.winfo_reqwidth() // 2)
        accessibility_label_y = (4.5 / 6) * self.root.winfo_screenheight()

        accessibility_label.place(x=accessibility_label_x, y=accessibility_label_y)

        return accessibility_label

    
    def create_speech_listening_label(self):
        
        speech_listening_label = tk.Label(self.root, text="Listening...", font=('Consolas', 16), bg="#1e1e1e", fg="white")
        return speech_listening_label
    
    def show_speech_listening_label(self):
        self.speech_listening_label_x = (self.root.winfo_screenwidth() // 2) - (self.speech_listening_label.winfo_reqwidth() // 2)
        self.speech_listening_label_y = (3.5 / 6) * self.root.winfo_screenheight()

        self.speech_listening_label.place(x=self.speech_listening_label_x, y=self.speech_listening_label_y)

    def hide_speech_listening_label(self):
        self.speech_listening_label.place_forget()

    def set_speech_input_button(self, status):
        if(status == "active"):
            image_path = Path(__file__).parent / "images/microphone_in_use.png"
        else:
            image_path = Path(__file__).parent / "images/microphone_idle.png"

        resized_image = self.resize_image(image_path, 40, 40)
        self.speech_input_button.config(image=resized_image)
        self.speech_input_button.image = resized_image

    def create_speech_input_button(self):

        def on_button_click():
            self.show_speech_listening_label()
            self.set_speech_input_button("active")
            self.update_chatbot_icon("images/chatbot_thinking.png")
            root.update()
            speech_input = stt.record_text()
            
            if(speech_input == "Request_Error"):
                chatbot.force_chatbot_response_audio("I'm sorry, there was an error with the request. Please try again.")
            elif(speech_input == "Unknown_Value_Error"):
                chatbot.force_chatbot_response_audio("I'm sorry, I didn't catch that. Please try again.")
            else:
                chatbot_response = chatbot.get_chatbot_response(speech_input)
                chatbot.generate_chatbot_response_audio(chatbot_response)

            self.hide_speech_listening_label()
            self.set_speech_input_button("idle")
            self.update_chatbot_icon("images/chatbot_idle.png")
            root.update()
            chatbot.play_chatbot_response_audio()
                
        image_path = Path(__file__).parent / "images/microphone_idle.png" 
        IMAGE_WIDTH = 40
        IMAGE_HEIGHT = 40 
        microphone_idle_icon = self.resize_image(image_path, IMAGE_WIDTH, IMAGE_HEIGHT)

        speech_input_button = tk.Button(self.root, image=microphone_idle_icon, font=('Arial', 16), command=on_button_click,bd=0)
        speech_input_button.image = microphone_idle_icon

        text_entry_x = (self.root.winfo_screenwidth() // 2) - (self.text_entry.winfo_reqwidth() // 2) - 40
        button_x = text_entry_x + self.text_entry.winfo_reqwidth() + 10
        button_y = (4 / 6) * self.root.winfo_screenheight()

        speech_input_button.place(x=button_x, y=button_y)
        return speech_input_button

    def create_chatbot_icon(self, image_file_name):

        image_path = Path(__file__).parent / image_file_name
        IMAGE_WIDTH = 300
        IMAGE_HEIGHT = 300 

        self.chatbot_icon_images[image_file_name] = self.resize_image(image_path, IMAGE_WIDTH, IMAGE_HEIGHT)

        chatbot_icon_label = tk.Label(self.root, image=self.chatbot_icon_images[image_file_name])
        chatbot_icon_label.config(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, borderwidth=0)

        chatbot_icon_label_x = (self.root.winfo_screenwidth() // 2) - (IMAGE_WIDTH // 2)
        chatbot_icon_label_y = ((5/6)*self.root.winfo_screenheight() // 2) - IMAGE_HEIGHT // 2

        chatbot_icon_label.place(x=chatbot_icon_label_x, y=chatbot_icon_label_y)

        return chatbot_icon_label

    def process_input(self, event):
        self.update_chatbot_icon("images/chatbot_thinking.png")
        self.root.update()

        input_text = self.text_entry.get()
        self.text_entry.delete(0, tk.END)

        chatbot_response = chatbot.get_chatbot_response(input_text)
        chatbot.generate_chatbot_response_audio(chatbot_response)

        self.update_chatbot_icon("images/chatbot_idle.png")
        self.root.update()

        chatbot.play_chatbot_response_audio()

    def update_chatbot_icon(self, image_file_name):
        image_path = Path(__file__).parent / image_file_name

        if image_file_name not in self.chatbot_icon_images:
            self.chatbot_icon_images[image_file_name] = self.resize_image(image_path, 300, 300)

        self.chatbot_icon_label.configure(image=self.chatbot_icon_images[image_file_name])
        self.chatbot_icon_label.image = self.chatbot_icon_images[image_file_name]
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)

    root.mainloop()