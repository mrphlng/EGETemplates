w = 0
max_count = 0
a = [0] * 100000
for n in range(1000):
    x = bin(n)[2:]
    z = bin(n % 4)[2:]
    y = x + z
    r = int(y, 2)
    a[r] = 1
for i in range(100000 - 49):
    max_count = max(max_count,sum(a[i:i + 49]))
print(max_count)