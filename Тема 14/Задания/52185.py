for x in range(37):
    r = 3 * 37 ** 3 + 1 * 37 ** 2 + 7 * 37 ** 1 + x * 37 ** 0 + 4 * 37 ** 3 + x * 37 ** 2 + 2 * 37 ** 1 + 9 * 37 ** 0
    if r % 36 == 0:
        print(r // 36)
        break