print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and z or not(w)) and x or y):
                    print(x,y,z,w,'0')
                if (x and z or not(w)) and x or y:
                    print(x,y,z,w,'1')