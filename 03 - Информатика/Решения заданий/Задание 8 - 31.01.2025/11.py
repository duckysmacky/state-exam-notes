from itertools import product

cnt = 0
for word in product("WXYZ", repeat=6):
    if word.count('Y') == 2:
        cnt += 1
print(cnt)
