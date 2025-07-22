from itertools import product

cnt = 0
for i, w in enumerate(product("АВИОРТФ", repeat=6), 1):
    word = ''.join(w)
    if i % 2 == 0 and word[0] != 'О' and word.count('Р') == 2:
        cnt += 1
print(cnt)
