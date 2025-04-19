from itertools import*
c = 0
for s in product('0123456789', repeat = 10):
    line = ''.join(s)
    if line[0] != '0' and line[0] != line[1] != line[2] != line[3] != line[4] != line[5] != line[6] != line[7] != line[8] != line[9] and int(s) % 5 == 0:
        c += 1
print(c)