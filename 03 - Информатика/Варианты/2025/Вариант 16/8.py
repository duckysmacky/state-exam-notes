from itertools import product

for i, word in enumerate(product(sorted("СОРНЯК"), repeat=6), start=1):
    if word.count('К') <= 3 and word.count('Я') == 2:
        print(i, ''.join(word))
        break
