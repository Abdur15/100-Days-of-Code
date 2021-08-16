class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.answer = ""
        self.correct = ""

    def still_has_question(self):
        if (self.question_number < len(self.question_list)):
            return True
        else:
            return False

    def next_question(self):
        self.answer = input(f"Q.{self.question_number + 1} : {self.question_list[self.question_number].text} (True/False)?\n").capitalize()
        self.check_answer()
        self.question_number += 1

    def check_answer(self):
        self.correct = self.question_list[self.question_number].answer
        if self.answer == self.correct:
            self.score += 1
            # return True
            print("You are Right !")
            print(f"The correct answer was {self.correct}")
            print(f"Your current score is :{self.score}/{self.question_number + 1}")
        else:
            print("Its Wrong !")
            print(f"The correct answer was {self.correct}")
            print(f"Your current score is :{self.score}/{self.question_number + 1}")














