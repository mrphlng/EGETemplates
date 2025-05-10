maxr = 0
for N in range(1,12):
    x = bin(N)[2:]
    if N % 2 == 0:
        x = '10' + x
    else:
        x = '1' + x +'01'
    R = int(x, 2)
    maxr = max(maxr, R)
print(maxr)