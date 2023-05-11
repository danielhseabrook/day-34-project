from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')
quiz = QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, height=800)


        self.label_score = Label(text=self.quiz.score, fg="white", bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Text", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.image_true = PhotoImage(file="images/true.png",)
        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.user_true)
        self.button_true.grid(row=2, column=0, pady=20)

        self.image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.user_false)
        self.button_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            print(f"You've completed the quiz.\nYour score is {self.quiz.score}")
            self.window.destroy()
        q_text = self.quiz.next_question()
        self.canvas.itemconfigure(self.question_text, text=q_text)

    def user_true(self):
        # self.questions_left()
        self.quiz.check_answer("True")
        self.get_next_question()
        self.label_score.config(text=self.quiz.score)

    def user_false(self):
        # self.questions_left()
        self.quiz.check_answer("False")
        self.get_next_question()

    # def questions_left(self):

