from itertools import product
count = 0
for str in product('АНДРЕЙ', repeat=7):
    line = ''.join(str)
    if line.count('А') == 1 and line.count('Й') == 1 and line[0] != 'Й':
        count += 1
print(count)
