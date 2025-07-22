R = range(2)
for w in R:
    for x in R:
        for y in R:
            for z in R:
                # (x == w) or (y and not z) or w
                if ((x == w) or (y and not z) or w) == 0:
                    print(x, w, z, y)
# w x y z
# 0 1 0 0
# 0 1 0 1
# 0 1 1 1
