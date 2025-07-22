r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = ((y <= x) == (w <= (not z))) and (w or x)
                if f:
                    print(x, y, z, w)
