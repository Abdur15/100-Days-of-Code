import pyautogui

import inputs
import random
from inputs import to_str
#import pyautoguia
logo = inputs.logo
print(logo)
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
print(f"Your Letter is {to_str(display).capitalize()}")
m=len(stages)
life = []
while "_" in display:
    guess = input("Enter your Guess :\n").lower()
    if guess not in word:
        life = stages[m - 1]
        print(f"Your Letter is {to_str(display).capitalize()}")
        print("You lose your life", life)
        m -= 1
        if m == 0:
            print("😐 😐 😐 You Hung the Man 😐 😐 😐 \n!!! You lose !!!")
            print(f"The word was {word.capitalize()}")
            break
    elif guess in display:
        print(f"Your Letter is {to_str(display).capitalize()}")
        print(f"The letter {guess} is already in the word\nChoose any other letter")
    else:
        for i in range(0, len(word)):
            if guess == word[i]:
                display[i] = guess
        print(f"Your Letter is {to_str(display).capitalize()}")
        if len(life) > 0:
            print("You lose your life", life)
    if "_" not in display:
        print("!!!! ✨ ✨ ✨ 🎊 🎊 🎊 Congrats You Win 🎊 🎊 🎊 ✨ ✨ ✨ !!!!\n👏 👏 👏")
    pyautogui.hotkey('=','`')