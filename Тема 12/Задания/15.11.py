for x in range(3,10000):
    s = '1' + x * '8'
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18','8',1)
        if '388' in s:
            s = s.replace('388','81',1)
        if '888' in s:
            s = s.replace('888','3',1)
    if s.count('1') == 3:
        print(x)
        break