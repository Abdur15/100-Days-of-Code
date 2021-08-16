from question_model import Question
from data import question_data
from quiz_brain import *
question_bank = []
for i in range(0,len(question_data)):
    a = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(a)

b = QuizBrain(question_bank)

print("Welcome to our Quiz !!!!")

while b.still_has_question():
     b.next_question()
     print("=" * 20)


print("You have completed the Quiz")
print(f"Your  final score is : {b.score}")












