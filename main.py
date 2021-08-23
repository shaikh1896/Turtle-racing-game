from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Which player will win', prompt='red/yellow/green/blue/grey')
colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
y_pos = [-80, -40, 0, 40, 80, 120]
all_turtles = []
for color in range(0, 6):
    the_turtle = Turtle(shape='turtle')
    the_turtle.color(colors[color])
    the_turtle.penup()
    the_turtle.goto(x=-240, y=y_pos[color])
    all_turtles.append(the_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! the {winning_color} turtle is the winner.')
            else:
                print(f'You lost! the {winning_color} turtle is the winner.')
        random_distance = random.randint(0, 10)
        turtle.speed('slow')
        turtle.forward(random_distance)


screen.exitonclick()