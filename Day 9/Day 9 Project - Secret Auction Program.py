import pyautogui
import logo1
logo = logo1.logo
print(logo)
a = "y"
bidder = {}
while a != "n":
    name = input("Enter Bidder's Name:\n")
    gender  = input("Enter your gender Male or Female")
    if gender == "Male":
        bidder_name = "Mr." + name
    else:
        bidder_name = "Mrs." + name
    bid = int(input("Enter your bid amount in USD :\n$"))
    bidder[bidder_name] = bid
    highest = 0
    for key in bidder:
        if bidder[key] > highest:
            highest = bidder[key]
            highest_bidder = key
    a = input("if you want to continue press y else n").lower()
    pyautogui.hotkey("=","`")
print(f'The Highest Bid is ${highest} sold to {highest_bidder}\nCongrats to {highest_bidder} and thanks for the bid.')









