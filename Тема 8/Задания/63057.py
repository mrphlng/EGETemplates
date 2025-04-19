from itertools import*
odd = '1357'
even = '2468'
count = 0
for line in product(even, odd, even, odd, even, odd, even, odd, even):
    line = ''.join(line)
    if line.count('1') <= 3 and line.count('2') <= 3 and line.count('3') <= 3 and line.count('4') <= 3 and \
            line.count('5') <= 3 and line.count('6') <= 3 and line.count('7') <= 3 and line.count('8') <= 3:
        count += 1
print(count * 2)
