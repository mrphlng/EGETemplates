from turtle import*
tracer(0)
k = 20
for x in range(4):
    fd(8 * k)
    right(90)
for x in range(3):
    fd(12 * k)
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k,y * k)
        dot(3)
exitonclick()