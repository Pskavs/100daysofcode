from tkinter import messagebox
import turtle
import pandas as pd
screen = turtle.Screen()

#Set Global Variables
CORRECT_STATES = []
SCORE = 0

#Reads the csv file in with pandas
STATES = pd.read_csv("50_states.csv")
#Creates a turtle object that writes the state name on the map when the user guesses correctly
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

#Sets up the screen with the US Map as a background.
screen.title(f"{SCORE} / 50 states correct")
background_image = "blank_states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)

def check_state(u_input):
    """Checks the user input against the csv list of states and the list of states they have already guessed.
    If it doesn't match either, they get a point and it is added to the map."""
    global SCORE
    global STATES
    print(u_input)
    if u_input in STATES.values and u_input not in CORRECT_STATES:
        correct_state = STATES[STATES['state']==u_input]

        #Removes the state from the list so that we can print a study sheet later.
        STATES = STATES.drop(STATES.loc[STATES['state']==u_input].index)

        #The - 15 is to correct the coordinates slightly.
        x_coordinate = correct_state['x'] - 20
        y_coordinate = correct_state['y'] - 15
        CORRECT_STATES.append(u_input)
        SCORE += 1
        screen.title(f"Correct! {SCORE} / 50 states correct.")
        writer.goto(int(x_coordinate.iloc[0]), int(y_coordinate.iloc[0]))
        writer.write(f"{u_input}")
    else:
        screen.title(f"Try again! {SCORE} / 50 states correct.")

# Creates the game loop
game_is_active = True
while game_is_active:
    if SCORE == 50:
        messagebox.showinfo( "WINNER!", "YOU WIN THE GAME! Great Job :)")
        game_is_active = False
        screen.bye()
    else:
        user_input = screen.textinput(title= "Guess State", prompt="What is the name of a U.S. state?")
        if user_input is None:
            game_is_active = False
        else:
            check_state(user_input.title())



print_study_sheet = ''
while print_study_sheet != 'y' and print_study_sheet != 'n':
    print_study_sheet = screen.textinput(title = "Study Sheet", prompt = "Would you like a study sheet? (Y / N)").lower()
    if print_study_sheet == 'y':
        print(STATES)
        STATES.to_csv("study_sheet.csv")
    elif print_study_sheet == 'n':
        screen.bye()
screen.mainloop()

