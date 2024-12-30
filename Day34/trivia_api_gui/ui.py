from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUIZ_FONT = ('Arial',20,'italic')
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        #Creates the window
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizzin")
        self.window.config(background=THEME_COLOR)
        
        #Creates the score label
        self.score_label = Label(self.window, text="Score:", background=THEME_COLOR, fg='white',font=20)
        self.score_label.grid(row=0, column=1,pady=(20,0))
        
        #Creates the center canvas where the quiz questions are
        self.canvas = Canvas(self.window, width=300, height=250,background='white')
        self.question_text = self.canvas.create_text(
            150,125,text="blah blah", fill=THEME_COLOR, font=QUIZ_FONT, width=280
        )
        self.canvas.grid(row=1, column=0,padx=20,pady=20, columnspan=2)
        
        #Creates the true / false buttons
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(
            bg=THEME_COLOR,highlightthickness=0,image=true_image, command= self.true_pressed
        )
        self.true_button.grid(row=2, column=1,padx=20,pady=20)
        self.false_button = Button(
            bg=THEME_COLOR, highlightthickness=0, image=false_image, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=0, padx=20, pady=20)

        self.get_next_question()
        #Keeps the window open
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text =q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

