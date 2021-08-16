MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def money_process():
    q_a  = 0.25
    d_a = 0.10
    n_a = 0.05
    p_a = 0.01
    print("Please insert coins.")
    q = int(input("how many quarters?"))
    d = int(input("how many dime?"))
    n = int(input("how many nickle?"))
    p = int(input("how many penny?"))
    if usr == 'espresso':
        rate = 1.50
    elif usr == "latte":
        rate = 2.50
    elif usr == "cappuccino":
        rate = 3.00
    amount_in = (q_a * q) + (d_a * d) + (n_a * n) + (p_a * p)
    if amount_in >= rate:
        change = amount_in - rate
        print("Here is ${:.2f} in change".format(change))
    else:
        return "na"

def espresso():
    cash_in = MENU["espresso"]["cost"]
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    return {
        "water": water,
        "milk": 0,
        "coffee": coffee,
        "cash": cash_in
    }

def latte():
    cash_in = MENU["latte"]["cost"]
    water = MENU["latte"]["ingredients"]["water"]
    milk = MENU["latte"]["ingredients"]["milk"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    return {
        "water": water,
        "milk": milk,
        "coffee": coffee,
        "cash": cash_in
    }
def cappuccino():
    cash_in = MENU["cappuccino"]["cost"]
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    return {
        "water": water,
        "milk": milk,
        "coffee": coffee,
        "cash": cash_in
    }


usr = input("What would you like? (espresso,latte,cappuccino)")
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0.00
if usr not in ["espresso", "latte", "cappuccino", "report"]:
    print("Enter a valid Menu")
else:
    while usr != "off":
        if usr == 'report':
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}ml\nMoney: ${money}")
        elif usr == "espresso":
            if water >= MENU["espresso"]["ingredients"]["water"] and coffee >= MENU["espresso"]["ingredients"]["coffee"]:
                a = money_process()
                if a != "na":
                    b = espresso()
                    print("Here is your Espresso 🍵. Enjoy!")
                    water = water - b["water"]
                    milk = milk - b["milk"]
                    coffee = coffee - b["coffee"]
                    money = money + b["cash"]
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry ,Not Enough Resources.")
                break
        elif usr == "latte":
            if water >= MENU["latte"]["ingredients"]["water"] and coffee >= MENU["latte"]["ingredients"]["coffee"] and milk >=MENU["latte"]["ingredients"]["milk"]:
                a = money_process()
                if a != "na":
                    b = latte()
                    print("Here is your Latte 🍵. Enjoy!")
                    water = water - b["water"]
                    milk = milk - b["milk"]
                    coffee = coffee - b["coffee"]
                    money = money + b["cash"]
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry ,Not Enough Resources.")
                break
        elif usr == "cappuccino":
            if water >= MENU["cappuccino"]["ingredients"]["water"] and coffee >= MENU["cappuccino"]["ingredients"]["coffee"] and milk >= MENU["cappuccino"]["ingredients"]["milk"]:
                a = money_process()
                if a != "na":
                    b = cappuccino()
                    print("Here is your Cappuccino 🍵. Enjoy!")
                    water = water - b["water"]
                    milk = milk - b["milk"]
                    coffee = coffee - b["coffee"]
                    money = money + b["cash"]
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry ,Not Enough Resources.")
                break
        usr = input("What would you like? (espresso,latte,cappuccino)")
