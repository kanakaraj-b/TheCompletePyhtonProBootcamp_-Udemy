# Challenge 1 extracting color from the jpg file

import colorgram

rgb_colors = []
colors = colorgram.extract('dot_painting.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


# Challenge 2 drawing dots

import random
import turtle
from colormap import rgb2hex


colors = [(193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]


spotty = turtle.Turtle()
spotty.shape("turtle")
spotty.penup()

spotty.setheading(220)
spotty.forward(350)
spotty.setheading(0)


total_dot = 100
spotty.speed("fastest")

for dots in range(1, total_dot+1):
    my_color = random.choice(colors)
    r = my_color[0]
    g = my_color[1]
    b = my_color[2]
    my_color_new = rgb2hex(r, g, b)
    spotty.dot(20, my_color_new)
    spotty.forward(50)

    if dots % 10 == 0:
        spotty.setheading(90)
        spotty.forward(50)
        spotty.left(90)
        spotty.forward(500)
        spotty.setheading(0)


turtle.exitonclick()
