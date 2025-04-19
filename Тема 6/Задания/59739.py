from turtle import*
k = 20
tracer(0)
for w in range(2):
    forward(3 * k)
    left(90)
    back(10 * k)
    left(90)
up()
back(10 * k)
right(90)
forward(8 * k)
left(90)
down()
for z in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y * k)
        dot(3)
exitonclick()