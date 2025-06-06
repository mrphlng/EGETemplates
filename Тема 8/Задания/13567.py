from itertools import*
count = 0
for str in product('ABCDE', repeat = 5):
    line = ''.join(str)
    if line[0] != 'E' and line[4] != 'A':
        count += 1
print(count)