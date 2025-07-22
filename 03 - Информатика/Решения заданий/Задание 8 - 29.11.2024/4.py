from itertools import product

for i, w in enumerate(product(sorted("ЮПИТЕР"), repeat=5), start=1):
    if i % 2 != 0 and w[0] != 'Р' and w.count('Ю') == 2:
        print(i)