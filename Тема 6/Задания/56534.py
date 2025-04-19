from turtle import *
tracer(1)
koef = 20
for i in range(3):
    fd(7 * koef)
    right(90)
fd(8 * koef)
for i in range(3):
    left(90)
    fd(5 * koef)
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()
