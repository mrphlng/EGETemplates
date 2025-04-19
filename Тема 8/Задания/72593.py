from itertools import*
count = 0
for str in product('0123456789ABCDEF', repeat = 8):
    line = ''.join(str)
    if line.count('0') == 2 and line.count('A') < 5 and line.count('B') < 5 and line.count('C') < 5 and \
            line.count('D') < 5 and line.count('E') < 5 and line.count('F') < 5 and line[0] != 0:
        count += 1
print(count)