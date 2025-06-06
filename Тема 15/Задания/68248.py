'''for A in range(1000):
    if all(((y < 20) <= (x > 70)) or not((x < A) <= (y > A)) for x in range(1000) for y in range(1000)):
        print(A)
        break'''

for A in range(1000):
    f = True
    for x in range(1000):
        for y in range(1000):
            if not(((y < 20) <= (x > 70)) or not((x < A) <= (y > A))):
                f = False
    if f:
        print(A)
        break