from itertools import product

cnt = 0
for word in product("ЕДОНК", repeat=4):
    if word.count("О") == 2:
        cnt += 1
print(cnt)
