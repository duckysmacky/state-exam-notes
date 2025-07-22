r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = (y <= z) and (w == (x <= y)) and not x
                if f:
                    print(y, z, w, x)
