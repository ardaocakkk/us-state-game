from hashlib import new
import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?: ").title()
    if user_guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if user_guess in all_states:
        guessed_states.append(user_guess)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == user_guess]
        timmy.goto(int(state_data.x),int(state_data.y))
        timmy.write(user_guess)



        
