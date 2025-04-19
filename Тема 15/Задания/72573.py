p = range(3, 43)
q = range(18, 91)
r = range(72, 115)
m = 200
for begin in range(200):
    for end in range(200):
        a = range(begin, end)
        if all((x in q) <= ((x not in p) <= (((x not in r) and (x not in a)) <= (x not in q))) for x in range(200)):
            m = min(m, end - begin)
print(m)