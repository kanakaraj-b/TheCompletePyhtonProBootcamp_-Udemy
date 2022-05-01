from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Turtle Race", prompt="Choose the color:")
colors = ['red', 'yellow', 'green', 'blue', 'indigo', 'violet']
y_position = [-80, -50, -20, 10, 40, 70]
my_turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    my_turtles.append(new_turtle)

if choice:
    race = True


while race:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == choice:
                print(f"You won!, the winning turtle is of color {winner}")
            else:
                print(f"You lost!, the winning turtle is of color {winner}")
        movement = random.randint(0, 10)
        turtle.forward(movement)


screen.exitonclick()
