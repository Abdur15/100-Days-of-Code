import data
import random
from logo5 import *
import pyautogui
def comp():
    if a['follower_count'] > b['follower_count']:
        return "a"
    else:
        return "b"
d = data.data
#print(len(d))
print(logo)
a = random.choice(d)
print(f"Compare A : {a['name']},{a['description']},{a['country']}")
#print(a['follower_count'])
d.pop(d.index(a))
#print(f"{len(d)} after first selection")
b = random.choice(d)
print(vs)
print(f"Compare B : {b['name']},{b['description']},{b['country']}")
#print(b['follower_count'])

usr = input("Who has more followers? Type A or B\n").lower()
pyautogui.hotkey('=','`')
if usr == "a" or usr == "b":
    comp_out = comp()
    if comp_out != usr:
        score = 0
        print(logo)
        print(f"Sorry that's wrong. Your Final Score is: {score}")
        pyautogui.hotkey('=','`')
    else:
        score = 0
        while comp_out == usr:
            print(logo)
            score += 1
            print(f"You're Right!.Your Current Score is: {score}")
            if comp_out == "a":
                a = a
                #print(len(d))
                print(f"Compare A : {a['name']},{a['description']},{a['country']}")
                #print(a['follower_count'])
                b = random.choice(d)
                print(vs)
                #print(f"{len(d)} after first selection")
                print(f"Compare B : {b['name']},{b['description']},{b['country']}")
                #print(b['follower_count'])
                comp_out = comp()
            elif comp_out == "b":
                d.append(a)
                #print(len(d))
                a = b
                d.pop(d.index(a))
                print(f"Compare A : {a['name']},{a['description']},{a['country']}")
                #print(a['follower_count'])
                b = random.choice(d)
                print(vs)
                #print(f"{len(d)} after first selection")
                print(f"Compare B : {b['name']},{b['description']},{b['country']}")
                #print(b['follower_count'])
                comp_out = comp()
            usr = input("Who has more followers? Type A or B\n").lower()
            pyautogui.hotkey('=','`')
        print(logo)
        print(f"Sorry that's wrong. Your Final Score is: {score}")
else:
    print("Invalid Entry Press 'A' or 'B' only")

