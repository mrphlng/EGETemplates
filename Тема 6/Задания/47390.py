from turtle import*
k = 20
tracer(0)
for x in range(12):
    right(60)
    forward( 1 * k)
    right(60)
    forward(1 * k)
    right(270)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x *k, y * k)
        dot(3)
exitonclick()