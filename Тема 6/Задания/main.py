from turtle import *
# Отключает анимацию черепахи (Рисунок выводится сразу)
tracer(0)
# Коэффициент, для увеличения масштаба изображения
koef = 20


right(45)
for i in range(7):
    forward(5 * koef)
    right(45)
    forward(10 * koef)
    right(135)

exitonclick()