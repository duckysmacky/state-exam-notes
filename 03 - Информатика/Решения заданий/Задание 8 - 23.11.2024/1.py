from itertools import product

for i, word in enumerate(product("ACDNY", repeat=4)):
    if ''.join(word) == "ANDY":
        print(i + 1)