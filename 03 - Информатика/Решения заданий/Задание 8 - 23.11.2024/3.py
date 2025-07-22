from itertools import product

cnt = 0
for i, word in enumerate(product("БЛАНК", repeat=6)):
    if word[0] == 'К' and word.count('Н') == 2:
        cnt += 1
print(cnt)