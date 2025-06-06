print('x y z w u f')
f = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    if not(((z <= w) and (y == (not(x)))) <= (u == (y or z))):
                        f == ((z <= w) and (y == (not(x)))) <= (u == (y or z))
                        print(x,y,z,w,u,f)