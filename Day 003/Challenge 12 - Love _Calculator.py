## Love Calculator

# Instructions

#You are going to write a program that tests the compatibility between two people.

#To work out the love score between two people:

#Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

#For Love Scores **less than 10** or **greater than 90**, the message should be:

#`"Your score is **x**, you go together like coke and mentos."`

#For Love Scores **between 40** and **50**, the message should be:

#`"Your score is **y**, you are alright together."`

#Otherwise, the message will just be their score. e.g.:

#`"Your score is **z**."`

#e.g.

#`name1 = "Angela Yu"`

#`name2 = "Jack Bauer"`

#T occurs 0 times

#R occurs 1 time

#U occurs 2 times

#E occurs 2 times

#Total = 5

#L occurs 1 time

#O occurs 0 times

#V occurs 0 times

#E occurs 2 times

#Total = 3

#Love Score = 53

#Print: "Your score is 53."

# Example Input 1
#name1 = "Kanye West"
#name2 = "Kim Kardashian"
# Example Output 1
#Your score is 42, you are alright together.

# Example Input 2
#name1 = "Brad Pitt"
#name2 = "Jennifer Aniston"
# Example Output 2
#Your score is 73.

#"Your score is 47, you are alright together."
#"Your score is 125, you go together like coke and mentos."
#"Your score is 54."

name_1 = input(("Enter your Name"))
name_2 = input(("Enter your Name"))

name = name_1+name_2
name = name.lower()

T = name.count('t')
R = name.count('r')
U = name.count('u')
E = name.count('e')

true = str(T + R + U + E)
print(true)

L = name.count('l')
O = name.count('o')
V = name.count('v')
E = name.count('e')

love = str(L + O + V + E)
print(love)

total = int(true + love)

if(total <= 10 or total >= 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif(40 <= total <= 50 ):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
