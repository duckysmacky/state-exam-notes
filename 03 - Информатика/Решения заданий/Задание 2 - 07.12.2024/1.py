r = range(2)
for x in r:
    for y in r:
        for z in r:
            f = (y or x) <= (z == y)
            if f == 0:
                print(x, y, z)
# 1 0 1
# 0 1 1
# 0 1 0