## Days in Month

# Instructions

#You are then going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.

#days_in_month(year=2022, month=2)

#And it will use this information to work out the **number of days in the month**, then **return** that as the **output**, **e.g.:**

#28

def is_leap(year):
    if(year%4==0  or year%400==0):
        return True
    else:
        return False
year = int(input("Enter the Year"))
month = int(input("Enter the Month"))
def day_in_month():
    months = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    if is_leap(year) is True:
        months[2] = 29
    return months[month]
a = day_in_month()
print(f"There are {a} days in the {month} month of the year {year}")