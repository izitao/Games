import turtle
import pandas

#INITIALIZATION 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) #CHANGES THE SHAPE OF THE SCREEN


def get_coordinates(state):
    '''Returns coordinates for guessed state'''
    global data
    state_values = data[data.state == state] #GETS THE DATAS FOR THE GUESSED STATE
    return (int(state_values.x), int(state_values.y))  # ←ALSO THE RETURN FUNCTION CAN BE LIKE THIS
'''    print(int(state_values.x))
    state_index = state_values.index[0] #GIVES THE INDEX OF THE STATE
    print(state_index)
    state_dict = data[data.state == state].to_dict() #RETURNS THE STATE DATAS IN FORM OF A DICTIONARY
    print(state_dict)
    return (state_dict["x"][state_index], state_dict["y"][state_index])'''
    #return (int(state_values.x), int(state_values.y)) #ALSO THE RETURN FUNCTION CAN BE LIKE THIS


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
score = 0
#print(data) #PRINTS STATES

#GAME LOOP
while len(states) > 0:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates = get_coordinates(answer_state)
        print(coordinates)
        t.goto(coordinates[0], coordinates[1])
        t.write(answer_state)
        states.remove(answer_state)


#States to learn
states_to_learn = pandas.Series(states)
states_to_learn.to_csv("States_to_learn.csv")

