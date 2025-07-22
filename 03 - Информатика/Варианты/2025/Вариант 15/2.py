r = range(2)
for x in r:
    for y in r:
        for z in r:
            f = (not x or not z) and (y <= x)
            if f:
                print(y, z, x)
