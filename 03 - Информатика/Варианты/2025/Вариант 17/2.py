from itertools import product, permutations

def f(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w

for n in product((0, 1), repeat=8):
    table = [
        (0, n[0], 0, n[1]),
        (0, n[2], n[3], n[4]),
        (n[5], 0, n[6], n[6])
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        result = [f(**dict(zip(letters, row))) for row in table]
        if result == [1, 1, 1]:
            print(''.join(letters))
