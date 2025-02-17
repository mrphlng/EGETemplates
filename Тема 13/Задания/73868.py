count = 0
ip = '206.123.209.193'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '206.123.210.118'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print(int('11010000', 2))
for i3 in range(256 - 252):
    for i4 in range(256):
        ip = f'206.123.{208 + i3}.{i4}'
        s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
        if s.count('1') == 15:
            count += 1
print(count)
