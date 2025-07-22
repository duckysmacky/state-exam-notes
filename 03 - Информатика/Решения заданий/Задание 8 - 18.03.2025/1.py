from itertools import product, permutations

for i, w in enumerate(product("АБМРУ", repeat=5), 1):
    word = ''.join(w)
    if word[0] == 'Р':
        print(i)
        break
