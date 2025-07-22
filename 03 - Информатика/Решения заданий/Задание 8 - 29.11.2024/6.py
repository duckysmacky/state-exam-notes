from itertools import product

cnt = 0
for i, w in enumerate(product("ABCD123", repeat=4), start=1):
    if sum(w.count(n) for n in "123") == 2:
        cnt += 1
print(cnt)