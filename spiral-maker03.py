import turtle
from time import sleep

wn = turtle.Screen()
x = 1
turtle1 = turtle.Turtle()
turtle1.color("green")
for d in range(43):
    turtle1.forward(x)
    turtle1.left(90)
    x = x * 1.1618

wn.exitonclick()
