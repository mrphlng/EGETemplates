from itertools import*
count = 0
for s in product('012345678', repeat = 5):
    line = ''.join(s)
    if int(line[0]) > int(line[1]) > int(line[2]) > int(line[3]) > int(line[4]):
        count += 1
print(count)