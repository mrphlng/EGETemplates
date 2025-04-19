from itertools import*
count = 0
a = 'ABCD'
b = 'XYZ'
s = product(b,a,a,a)
for i in s:
    count += 1
print(count)