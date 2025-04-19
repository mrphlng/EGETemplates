from itertools import*
c = 0
for s in product('012345678', repeat = 6):
    line = ''.join(s)
    if line[0] != '0' and line[0] != '1' and line[0] != '3' and line[0] != '5' and line[0] != '7' and line[5] != '2' and line[5] != '3' and line.count('1') >= 2:
        c += 1
print(c)