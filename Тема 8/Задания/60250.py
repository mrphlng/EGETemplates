from itertools import *

odd = '1357'
even = '0246'

"""
Вместо: line.count('0') <= 1 and line.count('2') <= 1 and line.count('3') <= 1and line.count('4') <= 1 and 
        line.count('5') <= 1 and line.count('6') <= 1 and line.count('7') <= 1
Можно написать так: len(set(line)) == len(line)
"""

count = 0
for line in product(odd, even, odd, even, odd):
    line = ''.join(line)
    if line[0] != '0' and line.count('1') == 0 and line.count('0') <= 1 and line.count('2') <= 1 and line.count('3') <= 1 \
        and line.count('4') <= 1 and line.count('5') <= 1 and line.count('6') <= 1 and line.count('7') <= 1:
        count += 1

for line in product(even, odd, even, odd, even):
    line = ''.join(line)
    if line[0] != '0' and line.count('1') == 0 and line.count('0') <= 1 and line.count('2') <= 1 and line.count('3') <= 1 \
            and line.count('4') <= 1 and line.count('5') <= 1 and line.count('6') <= 1 and line.count('7') <= 1:
        count += 1

print(count)