from itertools import*
c = 0
for s in product('ГЕПАРД', repeat = 5):
    line = ''.join(s)
    if line.count('Г') == 1 and line[0] != 'А' and line[4] != 'Е':
        c += 1
print(c)