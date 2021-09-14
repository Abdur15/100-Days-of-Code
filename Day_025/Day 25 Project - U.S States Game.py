import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state = data.state.tolist()

score = 0
states_answered = []
while score < 50:
    user_answer = str(screen.textinput(title=f"Guess the State {score}/50",
                                       prompt="What's another states name",)).title()

    if user_answer == "Exit":
        break
    elif user_answer in state:
        index = state.index(user_answer)
        a = data.loc[index]
        states_answered.append(a.state)
        state_name = turtle.Turtle()
        state_name.pu()
        state_name.hideturtle()
        state_name.goto(x=a.x, y=a.y)
        state_name.write(a.state)
        score +=1

missing_states = []
for i in state:
    if i not in states_answered:
        missing_states.append(i)
states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")