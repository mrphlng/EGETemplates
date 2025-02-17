ip = '102.9.140.219'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '255.255.192.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))