c = 0
for N in range(10,1001):
    x = bin(N)[2:]
    x1 = str(x)[1:]
    x2 = int(x1,2)
    zov = N - x2
    print(zov)
    '''считаем сколько разных значений получилось(7)'''