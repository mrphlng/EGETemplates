from itertools import permutations
count = 0
for str in permutations('СВЕТЛАНА', 8):
    line = ''.join(str)
    if line.count('АА') == 0:
        count += 1
print(count//2)