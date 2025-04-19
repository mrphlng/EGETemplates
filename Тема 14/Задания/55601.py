s = 0
for p in range(7, 50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y * p ** 2 + 4 * p ** 1 + y * p ** 0) + (y * p ** 2 + 6 * p ** 1 + 5 * p ** 0) == (x * p ** 3 + z * p ** 2 + 2 * p ** 1 + 3 * p ** 0):
                    print(x * p ** 2 + y * p ** 1 + z * p ** 0)