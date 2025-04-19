from turtle import *
tracer(0)
koef = 20
for i in range(6):
    fd(23 * koef)
    right(90)
    fd(7 * koef)
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()