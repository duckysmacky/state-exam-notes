from itertools import product

for i, word in enumerate(product("AEY", repeat=5)):
    if i + 1 == 50:
        print(''.join(word))