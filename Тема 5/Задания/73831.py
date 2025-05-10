for N in range(1000):
    x = bin(N)[2:]
    i = x.count('1')
    o = x.count('0')
    i1 = bin(i)[2:]
    o1 = bin(o)[2:]
    Z = i1 + o1
    R = int(Z, 2)
    print(N,x,R)
    if R == 214:
        print(N)
        break
    N += 1