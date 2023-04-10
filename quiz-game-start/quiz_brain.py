class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        ques_number = self.question_number
        answer = input(f"Q:{ques_number+1} {self.question_list[ques_number].text} (true or false): ")
        correct_answer = self.question_list[ques_number].answer
        self.question_number += 1
        self.check_answer(answer, correct_answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("your answer is correct.")
            self.score += 1
        else:
            print("your answer is not correct.")

        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}.")
        print("\n")
