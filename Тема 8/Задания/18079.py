from itertools import*
count = 0
for str in product('КОТ', repeat = 6):
    line = ''.join(str)
    if line.count('К') == 1:
        count += 1
print(count)