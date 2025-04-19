from turtle import*
tracer(0)
k = 20
x = 14
forward((x + 2) * k)
for y in range(4):
    forward(x * k)
    right(90)
    forward((x + 2) * k)
right(90)
forward(2 * x * k)
for y in range(4):
    right(90)
    forward((3 * x - 1) * k)
up()
for x in range( -k, k):
    for y in range( -k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()

for x in range(100):
    if (2 * x + 2) ** 2 + (3 * x - 1) ** 2 - (x + 2) * (2 * x) > 2000:
        print(x)
        break