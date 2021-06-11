print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Choose your path right or left")
path = input("Enter your choice")
if(path == 'right'):
    print("You fell into the Hole\n GAME OVER !!!")
elif(path == 'left'):
    print("Do you want to swim over or wait for the boat")
    choice_1 = input("Enter your Choice")
    if(choice_1 == 'swim'):
        print("You were attacked by trout\n GAME OVER !!!")
    elif(choice_1 == 'wait'):
        print("Choose which colour door you want go through Red or Blue or Yellow")
        choice_2 = input("Enter your colour")
        if(choice_2 == 'red'):
            print("You were burned by fire\n GAME OVER !!!")
        elif(choice_2 == 'blue'):
            print("You were eaten by beasts\n GAME OVER !!!")
        elif(choice_2 == 'yellow'):
            print("!!!! 🎊 🎊 🎊 ✨ ✨ ✨ Congrats You Win the Treasure !!!! 🎊 🎊 🎊 ✨ ✨ ✨")
else:
    print("Game Over")


