##Pizza Order
#Instructions
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.

#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25

#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

#Example Input
#size = "L"
#add_pepperoni = "Y"
#extra_cheese = "N"

#Example Output
#Your final bill is: $28.

print("WELCOME TO PIZZA CORNER !!!\n Here we serve three variant of Pizzas \n 1.Small Pizza\n 2.Medium Pizza\n 3.Large Pizza\n For small size press S\n For medium size press M\n For large size press L")
print("To add Peperoni press Y for yes or N for No")
print("For Extra Cheese press Y for yes or N for No")

pizza = input("Enter the Pizza variant you want")
peperoni = input("Do you prefer Peperoni")
cheese = input("Do you prefer Extra Cheese")
amount = 0
S =15
M =20
L =25
if(pizza =='S'):
    amount = S
    if(peperoni == "Y"):
        amount = amount + 2
        if (cheese == "Y"):
            amount = amount + 1
        else:
            amount = amount
    else:
        amount = S
        if(cheese == "Y"):
            amount = amount + 1
        else:
            amount = S
elif(pizza == 'M'):
    amount = M
    if (peperoni == "Y"):
        amount = amount + 3
        if (cheese == "Y"):
            amount = amount + 1
        else:
            amount = amount
    else:
        amount = M
        if (cheese == "Y"):
            amount = amount + 1
        else:
            amount = M
elif(pizza == 'L'):
    amount = L
    if (peperoni == "Y"):
        amount = amount + 3
        if (cheese == "Y"):
            amount = amount + 1
        else:
            amount = amount
    else:
        amount = L
        if (cheese == "Y"):
            amount = amount + 1
        else:
            amount = L
else:
    print("No Order Taken")

print(f'Your Final Bill Amount is ${amount}')



