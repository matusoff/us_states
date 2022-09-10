import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'file path for blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# #to get x, y coordinates on the map and save data to csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv(r'file path \50_states.csv')

states_list = data.state.to_list()
guessed_state = []

# make a pop-up window with the question
# screen.textinput(title="Guess the States", prompt="What's another state's name?")

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", 
                                    prompt="What's another state's name?").title()


    #using List Comprehension
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r'file path\states_to_learn')
        break


    if answer_state in states_list:
        guessed_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        data.state == answer_state
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(state_data.state.item())
        


screen.exitonclick()
