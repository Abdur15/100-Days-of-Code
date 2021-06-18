import inputs
import random
from inputs import to_str
print("!!!!! WELCOME TO HANGMAN !!!!!\nGuess the letter to save a life")
word_list = inputs.word_list
stages =inputs.stages
word = random.choice(word_list)
chosen_word = word
#print(word)
display = []
a = len(word)
n = 0
while n<a:
    display.append("_")
    n +=1
print(to_str(display))
m=len(stages)
life = []
while "_" in display:
    guess = input("Enter your Guess :\n").lower()
    if guess not in word:
        life = stages[m - 1]
        print(to_str(display))
        print("You lose your life", life)
        m -= 1
        if m == 0:
            print("😐 😐 😐 You Hung the Man 😐 😐 😐 \n!!! You lose !!!")
            print(f"The word was {word.capitalize()} ")
            break
    else:
        for i in range(0, len(word)):
            if guess == word[i]:
                display[i] = guess
        print(to_str(display))
        if len(life) > 0:
            print("You lose your life", life)
    if "_" not in display:
        print("!!!! ✨ ✨ ✨ 🎊 🎊 🎊 Congrats You Win 🎊 🎊 🎊 ✨ ✨ ✨ !!!!\n👏 👏 👏")
