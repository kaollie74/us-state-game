import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

data = pandas.read_csv("50_states.csv")

# load image using turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_input = screen.textinput(title=f"Guess the State: {len(guessed_states)}/50",
                                    prompt="What's another state's name?").capitalize()
    if answer_input.capitalize() == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("new_states_to_learn.csv")
        break
    # if answer_input is one of the states in all of U.S.
    if answer_input in all_states:
        guessed_states.append(answer_input)
        # Create Turtle
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        # get State Row from file
        state_data = data[data.state == answer_input]
        # send & write state name
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# states to learn.csv

