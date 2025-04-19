import turtle
from turtle import*
k = 20
tracer(1)
for x in range(1):
    turtle.circle(50,20 * k,20)
    turtle.seth(300)
    turtle.circle(50,280,20)
    turtle.seth(70)
    forward(200)
    turtle.circle(30, 180, 20)
    turtle.seth(250)
    forward(198)
exitonclick()
