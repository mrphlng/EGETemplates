from itertools import*
count = 0
for str in product('0123', repeat = 3):
    line = ''.join(str)
    if int(line[0]) + int(line[2]) > int(line[1]) and line[0] != '0':
        count += 1
print(count)