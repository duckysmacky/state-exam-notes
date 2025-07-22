from itertools import product, permutations

for i, w in enumerate(product("EIQTU", repeat=6), 1):
    word = ''.join(w)
    if i == 9115:
        print(word)
