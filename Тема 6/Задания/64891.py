from turtle import*
tracer(0)
k = 20
for x in range(4):
    for y in range(4):
        forward(6 * k)
        right(90)
    forward(10 * k)
    right(90)
    forward(3 * k)
up()
for x in range( -k, k):
    for y in range( -k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()