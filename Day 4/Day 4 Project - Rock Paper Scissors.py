rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Enter your choice 0 for Rock, 1 for Paper, 2 for Scissors")
sel = int(input("Enter the number"))
emoji = [rock,paper,scissors]
import random
game = [0, 1, 2]
comp = random.choice(game)


if(sel >= 3):
    print("Invalid Number")
elif(sel == comp):
    print("Your Selection")
    print(emoji[sel])
    print("Computer Selection")
    print(emoji[comp])
    print("Game Draw")

elif(sel == 1 and comp == 0):
    print("Your Selection")
    print(emoji[sel])
    print("Computer Selection")
    print(emoji[comp])
    print("You Won")

elif(sel == 2 and comp == 1):
    print("Your Selection")
    print(emoji[sel])
    print("Computer Selection")
    print(emoji[comp])
    print("You Won")

elif(sel == 0 and comp == 2):
    print("Your Selection")
    print(emoji[sel])
    print("Computer Selection")
    print(emoji[comp])
    print("You Win")
else:
    print("Your Selection")
    print(emoji[sel])
    print("Computer Selection")
    print(emoji[comp])
    print("You Lose")
