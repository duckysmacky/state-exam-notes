from itertools import product

for i, word in enumerate(product("АБМРУ", repeat=5), start=1):
    if word[0] == 'Р':
        print(i)
        break