from itertools import product

cnt = 0
for word in product("FORK", repeat=6):
    if word.count('R') > 0:
        cnt += 1
print(cnt)