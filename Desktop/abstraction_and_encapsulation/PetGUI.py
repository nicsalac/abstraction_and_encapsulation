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




