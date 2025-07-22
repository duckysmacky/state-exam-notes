from itertools import product

for i, word in enumerate(product("АБКЛОТУФ", repeat=6), start=1):
    if word[0] != 'У' and word.count('Ф') == 2 and word.count('А') <= 1:
        print(i)