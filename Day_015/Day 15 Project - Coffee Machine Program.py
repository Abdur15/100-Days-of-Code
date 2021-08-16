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
    amount_in = (0.25 * q) + (0.10 * d) + (0.05 * n) + (0.01 * p)
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
if usr not in ["espresso", "latte", "cappuccino", "report"]:
    print("Enter a valid Menu")
else:
    a ={
        "espresso" : espresso(),
        "latte": latte(),
        "cappuccino": cappuccino()
    }
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0.00

    while usr != "off":
        if usr == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")
        else:
            if water >= MENU[usr]["ingredients"]["water"]:
                m = money_process()
                if m != "na":
                    op = a[usr]
                    print(f"Here is your {usr} 🍵. Enjoy!")
                    water = water - op["water"]
                    milk = milk - op["milk"]
                    coffee = coffee - op["coffee"]
                    money = money + op["cash"]
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry ,Not Enough Resources.")
                break
        usr = input("What would you like? (espresso,latte,cappuccino)")


