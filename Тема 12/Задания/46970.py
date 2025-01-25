for n1 in range(100):
    for n2 in range(100):
        for n3 in range(100):
            s = "0" + "1" * n1 + "2" * n2 + "3" * n3 + "0"
            while "00" not in s:
                s = s.replace("01", "210", 1)
                s = s.replace("02", "3101", 1)
                s = s.replace("03", "2012", 1)
            if s.count("1") == 70 and s.count("2") == 56 and s.count("3") == 23:
                print(2 + n1 + n2 + n3)