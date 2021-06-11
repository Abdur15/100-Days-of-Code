## Treasure Map
# Instructions

#You are going to write a program which will mark a spot with an X.

#In the starting code, you will find a variable called ```map```.

#This ```map``` contains a nested list.
#When ```map``` is printed this is what the nested list looks like:
#['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

#In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:

#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']

#This is to try and simulate the coordinates on a real map.

#Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

#First your program must take the user input and convert it to a usable format.

#Next, you need to use it to update your nested list with an "x".

# Example Input 1

#column 2, row 3 would be entered as:

#23

# Example Output 1

#['⬜️', '⬜️', '⬜️']

#['⬜️', '⬜️', '⬜️']

#['⬜️', 'X', '⬜️']

# Example Input 2

#column 3, row 1 would be entered as:
#31

# Example Output 2

#['⬜️', '⬜️', 'X']

#['⬜️', '⬜️', '⬜️']

#['⬜️', '⬜️', '⬜️']


row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map  = [ row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

pos = input("Where do you want your Treasure")
a = int(pos[0])
b = int(pos[1])

map[a -1][b - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

