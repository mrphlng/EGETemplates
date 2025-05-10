from itertools import product
count = 0
for str in product('БОРИС', repeat=6):
    line = ''.join(str)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)

from itertools import*
s = set()
for i in permutations('МАРИНА', 6):
    a = ''.join(i)
    if a[0] not in 'АИ':
        s.add(a)
print(len(s))