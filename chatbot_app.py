import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

class MyApp:
    def __init__(self, root):
        self.root = root

        SCREEN_WIDTH = self.root.winfo_screenwidth()
        SCREEN_HEIGHT = self.root.winfo_screenheight()

        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.root.state('zoomed')

        self.root.title("Test")
        self.root.configure(bg="#1e1e1e")

        self.text_entry = self.create_text_input_box()
        self.create_chatbot_icon()

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
    
    def process_input(self, event):
        global stored_input
        input_text = self.text_entry.get()
        stored_input = input_text
        self.text_entry.delete(0, tk.END)

        print(stored_input)

    def create_chatbot_icon(self):
        image_file_name = "images/chatbot_icon.png"
        image_path = Path(__file__).parent / image_file_name
        IMAGE_WIDTH = 300
        IMAGE_HEIGHT = 300

        self.image = self.resize_image(image_path, IMAGE_WIDTH, IMAGE_HEIGHT)

        label = tk.Label(self.root, image=self.image)
        label.config(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, borderwidth=0)
        label.place(x=(self.root.winfo_screenwidth() // 2) - (IMAGE_WIDTH // 2),
                    y=((5/6)*self.root.winfo_screenheight() // 2) - IMAGE_HEIGHT // 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)

    root.mainloop()