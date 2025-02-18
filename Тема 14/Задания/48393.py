for x in range(8):
    for y in range(8):
        r = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
        if r % 117 == 0:
            print(r // 117)