from turtle import *



speed(10)

color("orange")
color("yellow")
color("green")
color("blue")
color("purple")

begin_fill()
number_of_sides = 100

angle= 360 / number_of_sides
for i in range(number_of_sides):
    forward(25)
    right(angle)


exitonclick()