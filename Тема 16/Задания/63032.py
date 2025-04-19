def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    elif n % 2 != 0:
        return f(n // 10)
count = 0
for k in range(10 ** 9, 2 * 10 ** 9):
    if f(k) == 0:
        count += 1
print(count)
