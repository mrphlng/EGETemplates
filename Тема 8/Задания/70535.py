from itertools import*
c = 0
for x in product('0123456789AB', repeat = 5):
    if x.count('7') == 1 and x.count('9') + x.count('A') + x.count('B') <= 3 and x[0] != '0':
        c += 1
print(c)