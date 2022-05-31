from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title(string="Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="Questions here!",
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, width=100, height=97,
                                   highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=2, column=1)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, width=100, height=97,
                                   highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() is True:
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.right_button.config(state="normal")
            self.wrong_button.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_text, text="THE END", fill=THEME_COLOR)
            # self.right_button.config(state=DISABLED)
            # self.wrong_button.config(state=DISABLED)

    def right_pressed(self):
        answer = "True"
        is_right = self.quiz.check_answer(user_answer=answer)
        self.give_feedback(is_right)

    def wrong_pressed(self):
        answer = "False"
        is_right = self.quiz.check_answer(user_answer=answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Highlights the window in green if answer is correct, in red if answer is wrong and moves to next question
        after 1000 milli-seconds"""
        self.right_button.config(state=DISABLED)
        self.wrong_button.config(state=DISABLED)
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        updated_score = self.quiz.score
        self.score.config(text=f"Score: {updated_score}")
        self.window.after(1000, func=self.next_question)
