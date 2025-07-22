from itertools import product, permutations

cnt = 0
for word in product("ПИТОН", repeat=7):
    if word[0] == 'П' and word.count('И') == 1:
        cnt += 1
print(cnt)
