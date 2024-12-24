from tkinter import *
from tkinter import Label
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Resets the timer, the text, and the checkmarks."""
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text= '')
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Checks to see how many work sessions / break sessions the user has had. If it is 0,2,4,6 then they work, if it
    is 1,3,5,7, then they take a break. At 8, it is a long break and then the program stops."""
    global REPS
    REPS += 1
    if REPS == 9:
        title.config(text="Done")
        REPS = 0
    elif REPS % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif REPS % 2 ==0:
        title.config(text="Break",fg = PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Uses thw window.after method to count down by seconds. It uses division with rounding and modulo division in
    order to calculate the minutes and seconds. If the minutes or seconds are less than 10, it prints a 0 in front so
    the count remains a consistent format. Checks how many sessions were completed and gives the number of checks."""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec= "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        window.attributes("-topmost", False)
    else:
        checkmark.config(text="✅"*math.floor(REPS/2))
        window.attributes("-topmost", True)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
#Creates the window for the program
window = Tk()
window.title("Python Pomodoro")
window.config(padx=100, pady=100,bg=YELLOW)

#Label
title = Label(window, text="Timer", fg=GREEN,font=(FONT_NAME,40, "bold"),bg=YELLOW)
title.grid(column=1, row=0)

#Creates the tomato with the timer text in the center.
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,125,text='00:00',font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)

#Creates the start button
start_button = Button(window, text="START",command=start_timer)
start_button.grid(column=0,row=2)

#Creates the reset button
reset_button = Button(window, text="RESET", command=reset_timer)
reset_button.grid(column=2,row=2)

#Creates the checkmark
checkmark = Label(window,fg='green')
checkmark.grid(column=1,row=3)

#Keeps the program open.
window.mainloop()