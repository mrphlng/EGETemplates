for n in range(2,10000):
    s = bin(n)[2:]
    s = str(s)
    sum1 = 0
    sum0 = 0
    for i in range(len(s)):
            if i % 2 != 0 and s[i] == "1":
                sum1 += 1
            if i % 2 == 0 and s[i] == "0":
                sum0 += 1