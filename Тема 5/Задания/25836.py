for N in range(1000):
    x = bin(N)[2:]
    x = str(x)
    if N % 2 == 0:
        x = x + '00'
    else:
        x = x + '11'
    r = int(x,2)
    if r < 134:
        print(N, r)