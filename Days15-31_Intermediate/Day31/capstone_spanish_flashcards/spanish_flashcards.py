#------------------------------------Initializing------------------------------------#
import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
timer = ''
vocab_word=''
import time
BACKGROUND_COLOR = "#B1DDC6"

#Checks to see if there is already a spanish flashcards file that the user has studied.
try:
    vocab_list= pd.read_csv('data/spanish_flashcards.csv').to_dict(orient='records')
except FileNotFoundError:
    vocab_list= pd.read_csv("data/spanish_top100.csv").to_dict(orient="records")

#---------------------------------Flashcard Function---------------------------------#
def next_flashcard(word_known):
    """Checks to see if there are any vocabulary words in the list to study, if there are, it will pick a word
    at random and display it. If the user knows the word, it is removed from the list."""
    global vocab_word,timer
    window.after_cancel(timer)
    if len(vocab_list) == 0:
        messagebox.showinfo(title="Congratulations!", message="All words are learned!")
    else:
        vocab_word = random.choice(vocab_list)
        flashcard.itemconfig(flashcard_image,image=spanish_image)
        flashcard.itemconfig(title_label, text="Spanish",fill="black")
        flashcard.itemconfig(word_label, text=vocab_word["Spanish"],fill="black")
        timer = window.after(3000, flip_card)
        if word_known == 1 and len(vocab_list) > 0:
            vocab_list.remove(vocab_word)
            pd.DataFrame(vocab_list).to_csv("data/spanish_flashcards.csv", index=False)

def flip_card():
    """After 3 seconds, the card is flipped. Users then mark yes or no if they know the word."""
    flashcard.itemconfig(flashcard_image,image=english_image)
    flashcard.itemconfig(title_label, text="English", fill="white")
    flashcard.itemconfig(word_label, text=vocab_word["English"], fill="white")
    window.after_cancel(timer)
#-----------------------------------------UI-----------------------------------------#
#Sets up the window.
window = Tk()
window.config(bg=BACKGROUND_COLOR,height=700,width=900)
window.title("Spanish Flashcards")

#Sets up the flashcard.
flashcard = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
spanish_image = PhotoImage(file="images/card_front.png")
english_image = PhotoImage(file="images/card_back.png")
flashcard_image = flashcard.create_image(400,268, image=spanish_image)
flashcard.grid(row=0,column=0,padx=50,pady=(50,0),columnspan=2)

#Creates the labels on the flashcard
title_label = flashcard.create_text(400,150,text="Title",font=("Arial",40,"italic"))
word_label = flashcard.create_text(400,263,text="word",font=("Arial",50,"bold"))

#Sets up the wrong and right button.
wrong_image=PhotoImage(file="images/wrong.png")
right_image=PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, command=lambda:next_flashcard(0))
right_button = Button(image=right_image, command=lambda:next_flashcard(1))
wrong_button.grid(row=1,column=0,padx=50,pady=(0,50))
right_button.grid(row=1,column=1,padx=50, pady=(0,50))

timer = window.after(0,next_flashcard,0)
#Keeps the window open
window.mainloop()
