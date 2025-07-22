R = range(2)
print("y w z x")
for x in R:
    for y in R:
        for z in R:
            for w in R:
                if (not (w or x or y) or ((y or z) and x or y and (w or z))) == 0:
                    print(y, w, z, x)
# y w z x
# 0 0 0 1
# 0 1 1 0
# 0 1 0 1
# 1 0 0 0
# 0 1 0 0