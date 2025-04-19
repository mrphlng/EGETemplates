from itertools import*
count = 0
for str in product('0123456789ABCDE', repeat = 8):
    line = ''.join(str)
    if line.count('0') == 2 and (line.count('A') + line.count('B') + line.count('C') + line.count('D') + line.count('E')) < 5 and \
            line[0] != 0:
        count += 1
print(count)