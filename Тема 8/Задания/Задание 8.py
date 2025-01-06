from itertools import product
count = 0
for str in product('ГЕПАРД', repeat = 5):
    line = ''.join(str)
    if line.count('Г') == 1 and line[0] != 'А' and line[4] != 'Е':
        count += 1
print(count)