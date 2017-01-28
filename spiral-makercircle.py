
d = input("enter amount of iterations: ")

import turtle
screen = turtle.Screen()
turtle0 = turtle.Turtle()
turtle0.color("dark blue")
x = 2

for c in range(int(d)):
    turtle0.forward(20 + int(x))
    turtle0.left(60)
    x = x + 4

screen.exitonclick()
