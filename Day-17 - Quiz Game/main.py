# ................................. Quiz Game ................................. #
# ..........Created and modified by N.S.Bhanuprakash on 24-03-2022 .............#

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_object = Question(question_text, question_answer)
    question_bank.append(question_object)
# print(question_bank[0].question_text)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    # quiz.check_answer(user_answer=user_answer)
print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
# print(bank1[0].question_text)
# print(question_data[0]["text"])
