from math import sqrt

x1 = int(input("Введите x1 для первой вершины: "))
y1 = int(input("Введите y1 для первой вершины: "))
x2 = int(input("Введите x2 для второй вершины: "))
y2 = int(input("Введите y2 для второй вершины: "))
x3 = int(input("Введите x3 для третьей вершины: "))
y3 = int(input("Введите y3 для третьей вершины: "))
a = sqrt((x2 - x1)**2 + (y2-y1)**2)
b = sqrt((x3 - x2)**2 + (y3-y2)**2)
c = sqrt((x1 - x3)**2 + (y1-y3)**2)
p = (a + b + c)/2
print("Периметр треугольника равен:",a + b + c)
print("Площадь треугольника равна:",sqrt(p * (p - a) * (p - b) * (p - c)))