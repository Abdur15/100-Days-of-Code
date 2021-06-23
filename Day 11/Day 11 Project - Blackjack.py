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
    b.append(random.choice(cards))
    n = 0
    while n < 1:
        a = random.choice(cards)
        if a == 11:
            b.append(1)
        else:
            b.append(a)
        n+=1
    return b
def comparotor(a,b):
    if a > b and a < 21 :
        return "You Win!!!"
    elif b > a and b < 21:
        return "Opponent Wins"
    elif a > b and a > 21:
        return "You went over. You Lose "
    elif b > a and b > 21:
        return "Your Opponent went over. You Win"
    elif a > b and a == 21:
        return "You have Blackjack. You Win"
    elif b > a and b == 21:
        return "Blackjack. Your Opponent Wins"
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
        print(f'Your Cards:{player_total} ,Current Score : {sum(player_total)}')
        com = random_card_list()
        print(f"Computer's First Card : {com[0]}")
        while sum(com) < 17:
            j = random.choice(cards)
            if sum(com) > 10 and j == 11:
                com.append(1)
            else:
                com.append(j)
        f = 'h'
        while f != 'n':
            if sum(player_total) >= 21:
                f = 'n'
            else:
                f = input("press y if you want to get another card else n\n")
                if f == 'y':
                    v = random.choice(cards)
                    if sum(player_total) > 10 and v == 11:
                        player_total.append(1)
                    else:
                        player_total.append(v)
                    print(f'Your Cards:{player_total} , Current Score : {sum(player_total)} ')
                    print(f"Computer's First Card : {com[0]}")
    s = comparotor(a=sum(player_total), b=sum(com))
    print(f'Computer Cards : {com}')
    print(f"Computer score is {sum(com)}")
    print(s)



