from itertools import*
count = 0
for s in product('ABCDEFX', repeat = 4):
    line = ''.join(s)
    if line.count('X') == 1:
        count += 1
print(count)