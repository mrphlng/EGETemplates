from itertools import product
count = 0
for str in product('БОРИС', repeat=6):
    line = ''.join(str)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)