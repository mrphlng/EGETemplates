from itertools import*
count = 0
for str in product('ABCX', repeat = 5):
    line = ''.join(str)
    if line.count('X') == 1:
        count += 1
print(count)