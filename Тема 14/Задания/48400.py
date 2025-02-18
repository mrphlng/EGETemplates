for i in range(10):
    r = int(f'95{i}2', 11) + int(f'{i}458', 12)
    if r % 136 == 0:
        print(r // 136)
        break
