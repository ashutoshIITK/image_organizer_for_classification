import os
import shutil
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

class ImageOrganizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Organizer")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.img_label = Label(self.frame)
        self.img_label.pack()

        self.repair_required_button = Button(self.frame, text="Repair Required", command=self.move_repair_required)
        self.repair_required_button.pack()

        self.repair_likely_button = Button(self.frame, text="Repair Likely", command=self.move_repair_likely)
        self.repair_likely_button.pack()

        self.normal_button = Button(self.frame, text="Normal", command=self.move_normal)
        self.normal_button.pack()

        self.quit_button = Button(self.frame, text="QUIT", command=self.frame.quit)
        self.quit_button.pack()

        self.folder_path = filedialog.askdirectory()
        self.image_files = [f for f in os.listdir(self.folder_path) if f.endswith('.jpg') or f.endswith('.png')]
        self.display_image()

    def display_image(self):
        if self.image_files:
            self.current_image = self.image_files.pop(0)
            img = Image.open(os.path.join(self.folder_path, self.current_image))
            img = img.resize((250, 250), Image.ANTIALIAS) # Resize the image
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img)
            self.img_label.image = img
        else:
            self.img_label.config(text="No more images!")

    def move_image(self, folder_name):
        dest_folder = os.path.join(self.folder_path, folder_name)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.move(os.path.join(self.folder_path, self.current_image), dest_folder)
        self.display_image()

    def move_repair_required(self):
        self.move_image("repair_required")

    def move_repair_likely(self):
        self.move_image("repair_likely")

    def move_normal(self):
        self.move_image("normal")

if __name__ == "__main__":
    root = Tk()
    app = ImageOrganizer(root)
    root.mainloop()
