from turtle import*
tracer(0)
k = 20
for x in range(7):
    forward(10 * k)
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k,y * k)
        dot(3)
exitonclick()
38