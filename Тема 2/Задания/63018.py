print("x y z w u")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    if not(((x <= y) and (z == (not(w)))) <= (u == (x or z))):
                        print(x,y,z,w,u)
print(' ')
print("x y z w u")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                for u in range(0, 2):
                    if not(((x <= y)and(z == (not(w)))) <= (u == (x or z))):
                        print(x, y, z, w, u)