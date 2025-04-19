for x in '0123456789AB':
    for y in '0123456789AB':
        k = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)
        if k % 99 == 0:
            print(k // 99)
            break