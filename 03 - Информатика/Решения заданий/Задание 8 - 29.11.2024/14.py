from itertools import product

cnt = 0
for length in range(2, 5 + 1):
    for word in product("КОСМ", repeat=length):
        if word == word[::-1]:
            cnt += 1
print(cnt)