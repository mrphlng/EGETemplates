from turtle import*
k = 30
screensize(10000, 10000, "white")
tracer(0)
for x in range(2):
    forward(21 * k)
    right(90)
    forward(27 * k)
    right(90)
up()
forward(9 * k)
right(90)
forward(10 * k)
left(90)
down()
for x in range(2):
    forward(86 *k)
    right(90)
    forward(47 * k)
    right(90)
up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
