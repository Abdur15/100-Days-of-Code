#Leap Year

# Instructions

#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

year = int(input("Enter the Year"))
if(year%4==0  or year%400==0):
    print(f"The Year {year} is a Leap Year")
else:
    print(f"The Year {year} is not a Leap Year")