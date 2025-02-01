ip = '255.255.240.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '224.23.253.138'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))