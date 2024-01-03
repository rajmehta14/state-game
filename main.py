
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S STATES GAME")

image = ("blank_states_img.gif")

screen.addshape(image)


turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guissed_state=[]

while len(guissed_state)<50:




    answer_text= screen.textinput(title=f"{len(guissed_state)}/50 Guess The State" , prompt="What's the another state name?").title()

    if answer_text == "Exit":
        missing_state=[]
        for state in all_states:
            if state not in guissed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_text in all_states:
        guissed_state.append(answer_text)

        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state==answer_text]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_text)




