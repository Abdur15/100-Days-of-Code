############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import logo3
import pyautogui
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def random_card_list():
    b = []
    n = 0
    while n < 2:
        a = random.choice(cards)
        b.append(a)
        n+=1
    return b
def comparotor(a,b):
    if a > b and a <= 21 :
        return "You Win!!!"
    elif b > a and b <= 21:
        return "Opponent Wins"
    elif a > b and a > 21:
        return "You went over. You Lose "
    elif b > a and b > 21:
        return "Your Opponent went over. You Win"
    elif a == b:
        return "Draw"

l = 'd'
while l != 'n':
    l = input("Do you want play Blackjack Game press 'y' for yes or 'n for no\n")
    logo = logo3.logo
    print(logo)
    pyautogui.hotkey('=', '`')
    if l == 'y':
        player_total = random_card_list()
        com = random_card_list()
        if sum(player_total) == 21 and len(player_total) == 2:
            print(f'Your Cards:{player_total} ,Current Score : {sum(player_total)}')
            print("You have Blackjack. You Win")
            print(f'Computer Cards : {com}')
            print(f"Computer score is {sum(com)}")
        elif sum(com) == 21 and len(com) == 2:
            print(f'Your Opponents Cards:{player_total} , Score : {sum(player_total)}')
            print("Blackjack. Your Opponent Wins")
            print(f'Computer Cards : {com}')
            print(f"Computer score is {sum(com)}")
        else:
            print(f'Your Cards:{player_total} ,Current Score : {sum(player_total)}')
            print(f"Computer's First Card : {com[0]}")
            if sum(com) == 22:
                k = round(random.random())
                com[k] = 1
            while sum(com) < 17:
                p = random.choice(cards)
                if sum(com) + p > 21 and 11 in com:
                    h = com.index(11)
                    com[h] = 1
                if sum(com) + p > 21 and p == 11:
                    com.append(1)
                else:
                    com.append(p)
            f = 'h'
            while f != 'n':
                if sum(player_total) >= 21 and len(player_total) > 2:
                    f = 'n'
                else:
                    f = input("press y if you want to get another card else n\n")
                    if f == 'y':
                        v = random.choice(cards)
                        if sum(player_total) + v > 21 and 11 in player_total:
                            g = player_total.index(11)
                            player_total[g] = 1
                        elif sum(player_total) + v > 21 and v == 11:
                            player_total.append(1)
                        else:
                            player_total.append(v)
                        print(f'Your Cards:{player_total} , Current Score : {sum(player_total)} ')
                        print(f"Computer's First Card : {com[0]}")
            s = comparotor(a=sum(player_total), b=sum(com))
            print(f'Computer Cards : {com}')
            print(f"Computer score is {sum(com)}")
            print(s)



