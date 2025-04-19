for x in range(2030):
    k = 3 ** 100 - x
    count = 0
    while k > 0:
        if k % 3 == 0:
            count += 1
        k = k // 3
    if count == 2:
        print(x)
        break