import turtle
import random
from time import sleep

turtle1 = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
colors = ("blue","red","green","pink","gray")
for s in range(5):
    x = 10
    c = random.randint(0,len(colors)-1)
    turtle1.color(colors[c])
    x_pos = random.randint(-300,300)
    y_pos = random.randint(-300,300)
    turtle1.pu()
    turtle1.setpos(x_pos,y_pos)
    turtle1.pd()
    for d in range(30):
            turtle1.left(137.5)
            turtle1.forward(float(x))
            x = x + 5


wn.exitonclick()
