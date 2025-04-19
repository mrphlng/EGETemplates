from itertools import product
s = product('АВЕ*****', repeat = 3)
cnt = 0
for i in s :
    p = ''.join(i)
    if p.count('В') == 1:
        cnt += 1
    if p.count('В') == 1 and p.count('А') == 0:
        print(cnt)
        break