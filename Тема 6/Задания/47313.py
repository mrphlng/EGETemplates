from turtle import*
tracer(0)
k = 20
for x in range(10):
    forward(9 * k)
    right(90)
    forward(2 * k)
    right(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y * k)
        dot(3)
exitonclick()