from itertools import*
count = 0
for str in product('012345678', repeat = 5):
    line = ''.join(str)
    if line.count('12') == 0 and line[0] != '0' and line.count('21') == 0 and line.count('3') == 2 and line.count('32') == 0 and line.count('23') == 0 \
        and line.count('52') == 0 and line.count('25') == 0 and line.count('72') == 0 and line.count('27') == 0:
        count += 1
print(count)