from turtle import*
k = 10
tracer(0)
down()
for i in range(2):
    forward(23 * k)
    right(90)
    forward(10 * k)
    right(90)
forward(3 * k)
left(90)
forward(12 * k)
right(90)
for i in range(2):
    forward(9 * k)
    right(90)
    forward(32 * k)
    right(90)
up()
for x in range(-2*k,2*k):
    for y in range(-2*k,2*k):
        dot(3)
        goto(x*k,y*k)
exitonclick()