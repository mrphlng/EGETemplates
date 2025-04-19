import turtle
from turtle import*
tracer(1)
k = 20
down()
for x in range(1):
    left(50)
    forward(5 * k)
    turtle.circle(2 * k, 10 * k, 100)
    right(135)
    turtle.circle(2 * k, 10 * k, 100)
    forward(5 * k)
    left(50)
exitonclick()
