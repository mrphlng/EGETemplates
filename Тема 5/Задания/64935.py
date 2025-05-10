for N in range(1, 1000):
    x = bin(N)[2:]
    R = x + (bin(N % 4)[2:])
    Z = int(R, 2)
    print(N,Z,Z // N)