import turtle
from turtle import *
tracer(1000)
k = 20
for i in range(5):
    turtle.seth(0)
    turtle.circle(5 * k,180)
    turtle.seth(90)
    turtle.circle(5 * k, 180)
    turtle.seth(180)
    turtle.circle(5 * k, 180)
    turtle.seth(270)
    turtle.circle(5 * k, 180)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y * k)
        dot(3)
exitonclick()