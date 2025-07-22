from itertools import product, permutations

for i, w in enumerate(product("ГЕЭ024", repeat=7), 1):
    word = ''.join(w)
    if word == 'ЕГЭ2024' or word == '2024ЕГЭ':
        print(i)
