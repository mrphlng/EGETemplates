for x in range(101,110):
    i = '1' * x
    while('111' in x):
        x = x.replace('111','22',1)
        x = x.replace('222','11',1)
        print(x)