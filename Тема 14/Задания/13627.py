print(bin(4**511+2**511-511)[2:].count('1'))

k = 4**511 + 2**511 - 511
s = 0
while k > 0:
    if k % 2 == 1:
        s += 1
    k = k // 2
print(s)