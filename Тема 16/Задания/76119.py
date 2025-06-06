values = [0] * 500000000

for i in range(len(values)):
    if i >= 10000:
        values[i] = 1
    elif i < 10000 and i % 2 == 0:
        values[i] = 2 * i + values[i + 1]
    elif i < 10000 and i % 2 != 0:
        values[i] = values[i + 2] + i
print(values[2022] - values[2025])
