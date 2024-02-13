import tkinter as tk
import chatbot_engine as chatbot
import tts_handling as tts

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

        self.text_entry = self.create_text_input_box()

        self.chatbot_icon_images = {}
        self.chatbot_icon_label = self.create_chatbot_icon("images/chatbot_idle.png")
        
        self.text_entry.bind("<Return>", self.process_input)


    def resize_image(self, image_path, new_width, new_height):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((new_width, new_height))
        return ImageTk.PhotoImage(resized_image)

    def create_text_input_box(self):
        text_entry = tk.Entry(self.root, width=40, font=('Arial', 18))
        text_entry.place(x=(self.root.winfo_screenwidth() // 2) - (text_entry.winfo_reqwidth() // 2),
                         y=(4 / 6) * self.root.winfo_screenheight())
        return text_entry
    
    def create_chatbot_icon(self, image_file_name):
        image_path = Path(__file__).parent / image_file_name
        IMAGE_WIDTH = 300
        IMAGE_HEIGHT = 300 

        self.chatbot_icon_images[image_file_name] = self.resize_image(image_path, IMAGE_WIDTH, IMAGE_HEIGHT)

        label = tk.Label(self.root, image=self.chatbot_icon_images[image_file_name])
        label.config(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, borderwidth=0)
        label.place(x=(self.root.winfo_screenwidth() // 2) - (IMAGE_WIDTH // 2),
                    y=((5/6)*self.root.winfo_screenheight() // 2) - IMAGE_HEIGHT // 2)
        return label


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