for i in '0123456789':
    r = int('95' + i + '2', 11) + int(i + '458', 12)
    if r % 136 == 0:
        print(r // 136)
        break
