from logo4 import *
logo = print(logo)
import random
def comp():
    if g == guess:
        return guess
    elif g < guess:
        return "Too Low"
    elif g > guess:
        return "Too High"
guess  = random.randint(1,100)
print("Welcome to the number guessing game\nI'm thinking of a number between 1 and 100")
#print(guess)
n = input("Choose difficulty press 'E' for Easy and 'H' for Hard\n").lower()
if n == "e":
    n = 10
else:
    n = 5
while n > 0:
    print(f"You have {n} attempts to guess")
    g = int(input("Make a Guess:\n"))
    s = comp()
    if s == guess:
        print(f'You got it right. The number was {guess}')
        break
    else:
        print(s)
    n -= 1
    if n == 0:
        print(f"You have ran out of guess. You Lose. The number was {guess}")
