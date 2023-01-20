from tkinter import *
from tkinter import messagebox
import pandas
import random

card_back = "images/card_back.png"
card_front = "images/card_front.png"
index = 0
flip_timer = None


# -------------------------- I REMEMBER --------------------------

def i_remember():

    global index
    norwegian_list.pop(index)
    english_list.pop(index)

    updated_dictionary = pandas.DataFrame(list(zip(norwegian_list, english_list)), columns=["Norwegian", "English"])


    updated_dictionary.to_csv("data/norwegian_words.csv", index=False)    

    create_flash_card()

# -------------------------- FLIP THE CARDS --------------------------

def flip_the_card():

    global index, flip_timer
    english_word = english_list[index]

    canvas.itemconfig(image_id, image=bg_back)
    canvas.itemconfig(title, text=f"English", fill="white")
    canvas.itemconfig(word, text=f"{english_word}", fill="white")
    

# -------------------------- NEW WORD --------------------------

def create_flash_card():

    global index, flip_timer
    window.after_cancel(flip_timer)

    norwegian_word =  random.choice(norwegian_list)
    
    index = norwegian_list.index(norwegian_word)

    canvas.itemconfig(image_id, image=bg_front)
    canvas.itemconfig(title, text=f"Norwegian", fill="black")
    canvas.itemconfig(word, text=f"{norwegian_word}", fill="black")
    flip_timer = window.after(3000, func=flip_the_card)

# -------------------------- UI --------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#b1ddc6")

flip_timer = window.after(3000, func=flip_the_card)

bg_front = PhotoImage(file=card_front)
bg_back = PhotoImage(file=card_back)

canvas = Canvas(width=800, height=526, bg="#b1ddc6", highlightthickness=0)
image_id = canvas.create_image(400, 262, image=bg_back)
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3, rowspan=3)


check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=i_remember)
check_button.grid(column=2, row=4)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=create_flash_card)
x_button.grid(column=0, row=4)

try:
    dictionary = pandas.read_csv("data/norwegian_words.csv")
except:
    messagebox.showinfo(title="No file", message="No more words to learn")
else:
    norwegian_list = dictionary.Norwegian.to_list()
    english_list = dictionary.English.to_list()

    create_flash_card()

window.mainloop()



   