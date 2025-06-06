from itertools import*
n = '1357'
for x in product('01234567', repeat = 12):
    if (x[0] != '0') ,and x.count('1') + x.count('3') + x.count('5') + x.count('7') == 3 and