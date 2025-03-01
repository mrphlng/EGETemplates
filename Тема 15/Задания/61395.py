for a in range(400, -1, -1):
    if any(not(((3 * x) + y > 48) or (x > y) or ((4 * x) + y < a)) for x in range(400) for y in range(400)):
        print(a)
        break