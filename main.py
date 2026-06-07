import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_word=0

def english_translation():
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=file[random_word]["English"],fill="white")

def right_button_function():
    next_card()
    del(file[random_word])

def wrong_button_function():
    next_card()

def next_card():
    global window_after,random_word
    window.after_cancel(window_after)
    canvas.itemconfig(canvas_image,image=card_front)
    random_word=random.randint(0, len(file)-1)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=file[random_word]["French"],fill="black")
    window_after=window.after(3000,english_translation)

try:
    file=pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    file=pandas.read_csv("data/french_words.csv").to_dict(orient="records")
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
canvas=Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file='./images/card_back.png')
right_image=PhotoImage(file='./images/right.png')
wrong_image=PhotoImage(file='./images/wrong.png')
canvas_image=canvas.create_image(400,263,image=card_front)
title=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text=file[0]["French"],font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_button=Button(image=wrong_image,highlightthickness=0,command=wrong_button_function)
right_button=Button(image=right_image,highlightthickness=0,command=right_button_function)

wrong_button.grid(row=1,column=0)
right_button.grid(row=1,column=1)

window_after=window.after(3000,english_translation)

window.mainloop()

pandas.DataFrame(file).to_csv("data/words_to_learn.csv",index=False)
