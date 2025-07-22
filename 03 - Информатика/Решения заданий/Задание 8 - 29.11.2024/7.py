from itertools import product

cnt = 0
for w in product("АЛГОРИТМ", repeat=7):
    if sum(w.count(l) for l in "ЛГРТМ") > sum(w.count(l) for l in "АОИ"):
        cnt += 1
print(cnt)