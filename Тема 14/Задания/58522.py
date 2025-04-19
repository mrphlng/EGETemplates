for p in range(100):
    for x in range(p):
        for y in range(p):
            s = (3 * p + 2) * (p + 4)
            r = x * p ** 2 + y * p + 2
            if s == r:
                print(y * p + x)