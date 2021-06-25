import data
import random
def comp():
    if a['follower_count'] > b['follower_count']:
        return "a"
    else:
        return "b"
d = data.data
#print(len(d))
a = random.choice(d)
print(f"Compare A : {a['name']},{a['description']},{a['country']}")
print(a['follower_count'])
d.pop(d.index(a))
#print(f"{len(d)} after first selection")
b = random.choice(d)
print(f"Compare B : {b['name']},{b['description']},{b['country']}")
print(b['follower_count'])

usr = input("Who has more followers? Type A or B\n").lower()
if usr == "a" or usr == "b":
    comp_out = comp()
    if comp_out == usr:
        score = 1
    else:
        score = 0
    while comp_out == usr:
        print(f"You're Right!.Your Current Score is: {score}")
        if comp_out == "a":
            a = a
            #print(len(d))
            print(f"Compare A : {a['name']},{a['description']},{a['country']}")
            print(a['follower_count'])
            b = random.choice(d)
            #print(f"{len(d)} after first selection")
            print(f"Compare B : {b['name']},{b['description']},{b['country']}")
            print(b['follower_count'])
            comp_out = comp()
        elif comp_out == "b":
            d.append(a)
            #print(len(d))
            a = b
            d.pop(d.index(a))
            print(f"Compare A : {a['name']},{a['description']},{a['country']}")
            print(a['follower_count'])
            b = random.choice(d)
            #print(f"{len(d)} after first selection")
            print(f"Compare B : {b['name']},{b['description']},{b['country']}")
            print(b['follower_count'])
            comp_out = comp()
        score += 1
        usr = input("Who has more followers? Type A or B\n").lower()
    print(f"Sorry that's wrong. Your Final Score is: {score}")
else:
    print("Invalid Entry Press 'A' or 'B' only")

