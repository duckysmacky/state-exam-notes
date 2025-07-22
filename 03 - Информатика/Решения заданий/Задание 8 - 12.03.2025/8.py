from itertools import product, permutations

cnt = 0
for word in product("LOCK", repeat=7):
    if word.count('O') > 1:
        cnt += 1
print(cnt)
