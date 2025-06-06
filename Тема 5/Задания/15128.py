for x in range(9999,1001,-1):
    s = str(x)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    fer = str(k1 + k2 + k3 - min(k1,k2,k3) - max(k1,k2,k3))
    sec = str(max(k1,k2,k3))
    z = fer + sec
    if z == '1315':
        print(x)
        break