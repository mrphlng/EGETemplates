# I способ
for x in '0123456789abcdefghijkl':
    res = int(f'63{x}59685', 22) + int(f'17{x}53', 22) + int(f'36{x}5', 22)
    if res % 21 == 0:
        res = res // 21
        print(res)
        break


# II способ (При СС > 36)
def to_dec(values, base):
    s = 0
    index = len(values) - 1
    for i in range(len(values)):
        s += values[index] * base ** i
        index -= 1
    return s

# Можно было бы написать так: return sum(values[-(i + 1)] * base ** i for i in range(len(values)))

for x in range(22):
    res = (to_dec([6, 3, x, 5, 9, 6, 8, 5], 22) +
           to_dec([1, 7, x, 5, 3], 22) +
           to_dec([3, 6, x, 5], 22))
    if res % 21 == 0:
        res = res // 21
        print(res)
        break