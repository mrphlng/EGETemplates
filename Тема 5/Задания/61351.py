for N in range(45138888,45138889):
    x = bin(N)[2:]
    x1 = x + bin(N % 3)[2:][-2:].zfill(2)
    x2 = x1 + bin(int(x1, 2) % 5)[2:][-3:].zfill(3)
    R = int(x2,2)
    print(N, R, R // N)
n = 0
print(len(range(34722222,45138887)))

print((1444444416 - 1111111110) // 32)
print(1444444416 // 32)
print(1111111110 // 32)