from itertools import*
count = 0
for s in product('СВЕТА', repeat = 5):
    line = ''.join(s)
    if line.count('С') != 0:
        count += 1
print(count)