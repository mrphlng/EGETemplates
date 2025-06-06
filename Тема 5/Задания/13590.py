for x in range(100,1000):
    s = str(x)
    k1 = int(s[0]) * int(s[1])
    k2 = int(s[1]) * int(s[2])
    first = str(max(k1,k2))
    second = str(min(k1,k2))
    w = first + second
    if w == '205':
        print(x)
        break