n = int(input())
f = True
for i in range(2, n):
    if n % i == 0:
        f = False
        break
if f:
    print('Число простое')
else:
    print('Число составное')