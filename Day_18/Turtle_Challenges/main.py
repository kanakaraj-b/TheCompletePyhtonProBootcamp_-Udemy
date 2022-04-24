import random
import turtle
from turtle import Turtle, Screen

spotty = Turtle()
spotty.shape("turtle")

# Challenge 1
spotty.color("red")
for i in range(10):
    spotty.pencolor("red")
    spotty.forward(6)
    spotty.pencolor("white")
    spotty.forward(6)


# Challenge 2

import random
colors = ['red', 'blue', 'green', 'black', 'pink', 'purple', 'magenta']

for i in range(3, 10):
    p_color = random.choice(colors)
    spotty.color(p_color)
    sides = 360/i
    for j in range(i):
        spotty.forward(50)
        spotty.right(sides)


#Challenge 3

turtle.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tup = (r, g, b)
    return my_tup

move = ['right', 'left']
angle = [90, 180, 90, 360]
dist = [20, 10, 30, 50]
for i in range(50):
    spotty.width(10)
    spotty.color(colors())
    spotty.forward(random.choice(dist))
    moves = random.choice(move)
    spotty.setheading(random.choice(angle))


# Challenge 4
spotty.speed('fastest')

def draw_patteren(gap_value):
    for i in range(360//gap_value):
        spotty.color(colors())
        spotty.circle(100)
        spotty.setheading(spotty.heading() + gap_value)
        spotty.circle(100)


draw_patteren(5)

screen = Screen()
screen.exitonclick()

