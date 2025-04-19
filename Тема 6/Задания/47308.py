from turtle import*
tracer(0)
k = 20
for w in range(5):
    forward( 8 * k )
    right(60)
    forward( 8 * k )
    right(120)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x * k,y * k)
        dot(3)
exitonclick()