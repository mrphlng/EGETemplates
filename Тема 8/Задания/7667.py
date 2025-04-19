from itertools import*
c = 0
for s in product('ЕГЭ', repeat = 5):
    line = ''.join(s)
    if line[0] != 'Г':
        c += 1
print(c)