from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def repo(a):
    a = {'water': 300, 'milk': 200, 'coffee': 100}
    # print(report1)
    rep = []
    for i in a.keys():
        out = a[i] - c[i]
        rep.append(out)
    n = 0
    while(n<3):
        for j in a.keys():
            a[j] = rep[n]
            n+=1
    return a

items = Menu().get_items()
usr = input(f"What would like to drink?{items}")
if usr == "report":
    ing = CoffeeMaker().report()
    report2 = MoneyMachine().report()
else:
    while(usr != 'off'):
        report1 = {'water': 300, 'milk': 200, 'coffee': 100}
        if usr not in ["espresso","latte","cappuccino","report"]:
            order = Menu().find_drink(usr)
            break
        else:
            order = Menu().find_drink(usr)
            check = CoffeeMaker().is_resource_sufficient(order)
            if check is True:
                payment = MoneyMachine().make_payment(order.cost)
                if payment is True:
                    c = order.ingredients
                    coffee = CoffeeMaker().make_coffee(order)
                    a = repo(a=report1)
                    print(c)
                    print(a)
        report1 = a
        usr = input(f"What would like to drink?{items}")



