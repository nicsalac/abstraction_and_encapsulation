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

    self.label_type = tk.Label(window, text="Enter your pet's type(Dog, Cat, Bird):", font=my_font, fg="#5C3C28", bg="#F3EFEF")
    self.label_type.grid(row=1, column=0)

    self.entry_type = tk.Entry(window, font=my_font, bg="#FFFFFF")
    self.entry_type.grid(row=1, column=1)

    self.label_age = tk.Label(window, text="Enter your pet's age", font=my_font, fg="#5C3C28", bg="#F3EFEF")
    self.label_age.grid(row=2, column=1)

    self.entry_age = tk.Entry(window, font=my_font, bg="#FFFFFF")
    self.entry_age.grid(row=2, column=1)

    self.submit_button = tk.Label(window, text= "", font=my_font, fg="#5C3C28", bg="#FFDAA")
    self.submit_button.grid (row=4, columnspan=2, pady=20)

    self.result_label = tk.Label(window, text= "", font=my_font, fg="#5C3C28", bg="#F3EFEF")
    self.result_label.grid(row= 4, columnspan= 2)
    self.result_label.grid_remove()
    
    def submit(self):
        #create an object of the claas Pet and set attributes from GUI components"
        my_pet = Pet()
        my_pet.set_name(self.entry_name.get())
        my_pet.set_animal_type(self.entry_type.get())
        my_pet.set_age(int(self.entry_age.get()))

        







