r = 729 ** 8 - 3 ** 18 + 85
s = ""
while r != 0:
    s += str(r % 9)
    r //= 9
s = s[::-1]
print(s.count("0"))