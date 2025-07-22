r = range(2)
print("x y z w")
for x in r:
    for y in r:
        for z in r:
            for w in r:
                if ((not (x and y) or not z) and (not x or y) or w) == 0:
                    print(x, z, w, y)
# ? ? ? ?
# - 0 0 -
# 1 - 0 1
# - 1 0 0

# x z w y
# 1 0 0 0
# 1 1 0 1
# 1 1 0 0
