for x in '12345678':
    for y in '012345678':
        i = int('2' + y + '66' + x,9) + int(x + '0' + y + '1',12)
        if i%170 == 0:
            print(i//170)