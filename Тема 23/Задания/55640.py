def f(x,y,k1,k2,k3,k4):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1,y,k1 + 1,k2,k3,k4) + f(x + 2,y,k1,k2 + 1,k3,k4) + f(x * 2,y,k1,k2,k3 + 1,k4) + f(x * 3,y,k1,k2,k3,k4 + 1)
print(f(1,24,0,0,0,0))