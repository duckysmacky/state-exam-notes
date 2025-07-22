from itertools import product

for i, w in enumerate(product(sorted("ЛАСТ"), repeat=5), start=1):
    w = ''.join(w)
    if w.count('С') == 2 and 'Л' not in w and "ТТ" not in w:
        print(i)