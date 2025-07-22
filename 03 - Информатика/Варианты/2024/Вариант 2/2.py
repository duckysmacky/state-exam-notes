r = range(2)
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if (not x or z) and (w and (not y == z)):
                    print(w, x, y, z)
# 1 0 0 1
# 1 1 0 0
# 1 0 1 1