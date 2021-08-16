#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

amount = int(input("Enter the Bill Amount"))
number_of_person = int(input("Enter the number of people"))
bill  = (amount/number_of_person)*1.12

print("Your individual bill amount is {:.2f}".format(bill))