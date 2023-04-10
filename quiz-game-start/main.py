from data import questions
from question_model import Question
from quiz_brain import QuizBrain
question_banks = []
for question in questions:
    question_banks.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_banks)
while quiz.has_question():
    quiz.next_question()
print("You've completed the quiz.🤗")
print(f"your final score is {quiz.score}/{quiz.question_number}")
