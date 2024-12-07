from math import sqrt

a = float(input())
b = float(input())
c = float(input())
h = max(a, b, c)
k1 = min(a, b, c)
k2 = (a + b + c) - (h + k1)
if (k1 + k2) <= h: print("Не существует")
elif sqrt(h**2 - k1**2) == k2:
    print("Треугольник прямоугольный")
elif sqrt(h**2 - k1**2) < k2:
    print("Треугольник остроугольный")
else:
    print("Треугольник тупоугольный")

