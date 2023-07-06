import tkinter as tk
from tkinter import font
#importing class and modules
from Pet import Pet

class PetGUIComponents:
    #methods that create GUI components
    def  __init__(self, window):
        self.window = window
        window.title("Pet Society")
        window.geometry("500x300")
        window.configure(bg= "#F3EFEF")

    my_font = font.Font(font= 'Arial', size= 12)

    #Pet Information input and submit button
    self.label_name = tk.Label(window, text="Enter your pet's name:", font=my_font, fg="#5C3C28", bg= "#F3EFEF")
    self.label_name.grid(row=0, column=1)

    self.entry_name = tk.Entry(window, font=my_font, bg="#FFFFFF")
    self.entry_name.grid(row=1, column=0)

    




