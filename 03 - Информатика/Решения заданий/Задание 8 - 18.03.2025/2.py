from itertools import product, permutations

for i, w in enumerate(product("АЙЛФ", repeat=4), 1):
    word = ''.join(w)
    if word.count('А') == 0 and word.count('Л') == 0:
        print(i)
        break
