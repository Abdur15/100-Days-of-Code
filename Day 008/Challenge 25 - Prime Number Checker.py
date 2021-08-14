print("Prime Number Checker")
import time

def prime_number_checker(number):
    b =[]
    for i in range(1, number):
        a = number % i
        if a == 0:
            b.append(i)
    if len(b) > 2:
        print(f"The {number} is not prime")
    else:
        print(f"The {number} is prime")

a =int(input("Enter a  number to check :"))
t1 = time.time()
prime_number_checker(number=a)
t2 = time.time()
tot = t1 - t2
print(tot)
