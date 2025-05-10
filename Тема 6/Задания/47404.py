from turtle import*
tracer(0)
k = 20
screensize(2000,2000)
for x in range(4):
    forward( 10 * k)
    right(90)
right(30)
for x in range(5):
    forward(6 * k)
    right(60)
    forward(6 * k)
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k, y * k)
        dot(3)
exitonclick()