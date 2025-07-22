from itertools import product

combs = list(product("ЕКОР", repeat=6))

for n in range(len(combs)):
    comb = combs[n]
    if comb[0] == 'О' and all(comb[i] != comb[i + 1] != 'E' for i in range(len(comb) - 1)):
        print(n + 1, "".join(comb))
        break