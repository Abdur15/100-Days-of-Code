## Your Life in Weeks

# Instructions

#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.



#Where x, y and z are replaced with the actual calculated numbers.
#Example Input
#56
#Example Output
#You have 12410 days, 1768 weeks, and 408 months left.

year = int(input("Enter your current age"))
years_rem = 90-year

days_rem = years_rem*365
weeks_rem = years_rem*52
month_rem = years_rem*12

print(f'You have {days_rem} days, {weeks_rem} weeks, and {month_rem} months left')









