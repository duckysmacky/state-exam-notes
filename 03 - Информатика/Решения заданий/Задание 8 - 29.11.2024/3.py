from itertools import product

cnt = 0
for i, w in enumerate(product(sorted("МОНТАЖЕР"), repeat=6), start=1):
    if w[0] == 'О' and w.count('Ж') in (2, 3) and i % 3 == 0:
        cnt += 1
print(cnt)