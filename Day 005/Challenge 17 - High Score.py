## Highest Score

# Instructions

#You are going to write a program that calculates the highest score from a List of scores.

#e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

#**Important** you are not allowed to use the max or min functions. The output words must match the example. i.e

#> `The highest score in the class is: x`

# Example Input
#78 65 89 86 55 91 64 89

#In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`

# Example Output

#The highest score in the class is: 91

score = input("Enter the Scores")
h = score.split(",")
list = []
n = 0
for i in h:
    list.append(int(h[n]))
    n = n + 1
highest_score = 0
for j in list:
    if j > highest_score:
       highest_score = j
print(f"The highest score in the class is: {highest_score}")


