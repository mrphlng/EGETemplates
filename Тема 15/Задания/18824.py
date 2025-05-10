for A in range(300):
    k = 0
    for x in range(11):
        for y in range(11):
            if (x * y < A) or (y > x) or (x >= 8):
                k += 1
    if k == 121:
        print(A)
        break