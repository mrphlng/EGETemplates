from itertools import product

odd = '1357'
even = '2468'

count = 0
for line in product(odd, even, odd, even, odd, even, odd, even, odd, even, odd):
    line = ''.join(line)
    if line.count('1') < 5  and line.count('2') < 5  and line.count('3') < 5  \
            and line.count('4') < 5  and line.count('5') < 5  and line.count('6') < 5  and line.count('7') < 5 \
            and line.count('8') < 5:
        count += 1
print(count * 2)