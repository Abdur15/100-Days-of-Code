## Average Height

# Instructions

#You are going to write a program that calculates the average student height from a List of heights.

#e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

#e.g.

#180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

#There are a total of **7** heights in `student_heights`

#1146 ÷ 7 = **163.71428571428572**

#Average height rounded to the nearest whole number = **164**

#**Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input

#156 178 165 171 187

#In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output

#171

heights = input("Enter you Heights in m")
h = heights.split(",")
n = 0
m = 0
sum = 0
list = []
for i in h:
    list.append(int(h[n]))
    n = n + 1
for j in list:
    sum += list[m]
    m = m + 1

avg_heigt = round(sum/n)
print(f"The average height is {avg_heigt}")
print(sum)










