r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                f = not w and (x and not z or not x and not y and z)
                if f:
                    print(z, w, y, x)
