for a in range(400, -1, -1):
    if all((48 != y + 2 * x) or (a < x) or (a < y) for x in range(400) for y in range(400)):
        print(a)
        break