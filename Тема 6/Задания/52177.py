from turtle import*
k = 20
tracer(0)
for x in range(4):
    forward(6 * k)
    right(90)
    forward(6 * k)
    left(90)
    forward(6 * k)
    right(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y * k)
        dot(3)
exitonclick()