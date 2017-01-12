import turtle
from time import sleep

turtle1 = turtle.Turtle()
turtle1.color("blue")
x = 10
wn = turtle.Screen()
wn.bgcolor("lightgreen")
for d in range(50):
    turtle1.left(137.5)
    turtle1.forward(float(x))
    x = x + 5
wn.exitonclick()
