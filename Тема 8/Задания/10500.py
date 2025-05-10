from itertools import*
s = '12345'
count = 0
for x in product(s, repeat = 5):
    if x.count('1') == 3:
        count += 1
        print(count)