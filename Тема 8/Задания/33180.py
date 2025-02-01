from itertools import product
count = 0
for str in product('ТИМОФЕЙ', repeat=5):
    line = ''.join(str)
    if line.count('Й') < 2 and line[4] != 'Й' and line[0] != 'Й' and line.count('ИЙ') == 0 and line.count('ЙИ') == 0:
        count += 1
print(count)