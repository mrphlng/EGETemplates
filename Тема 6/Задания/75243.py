from turtle import*
k = 20
screensize(1000,1000)
tracer(0)
for x in range(3):
    forward(19 * k)
    right(90)
    forward(3 * k)
    right(90)
for x in range(3):
    forward(5 * k)
    right(90)
    forward(11 * k)
    right(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k,y * k)
        dot(3)
exitonclick()
28