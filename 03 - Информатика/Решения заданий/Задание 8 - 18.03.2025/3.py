from itertools import product, permutations

cnt = 0
for i, w in enumerate(product("АЕЖМНОРТ", repeat=6), 1):
    word = ''.join(w)
    if word[0] == 'О' and (word.count('Ж') == 2 or word.count('Ж') == 3) and i % 3 == 0:
        cnt += 1
print(cnt)
