from itertools import*
c = 0
for s in product('КОНФЕТА', repeat = 5):
    line = ''.join(s)
    if line.count('Е') == 2 and line[1] != 'Ф':
        c += 1
print(c)