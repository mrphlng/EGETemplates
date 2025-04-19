from turtle import*
tracer(0)
k = 20
for x in range(3):
    forward(20 * k)
    right(90)
    forward(4 * k)
    right(90)
for y in range(3):
    forward(6 * k)
    right(90)
    forward(13 * k)
    right(90)
up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()