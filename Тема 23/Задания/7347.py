def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1,y) + f(x * 2,y) + f(2 * x + 1,y) + f(x * 10,y)
print(f(1,14))