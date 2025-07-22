from itertools import product, permutations

def f(x, y, z, w):
    return ((y <= x) <= (z <= w))

for n in product((0, 1), repeat=6):
    table = [
        (n[0], 1, 1, 1),
        (n[1], 1, n[2], 1),
        (n[3], 1, n[4], n[5])
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        result = [f(**dict(zip(letters, row))) for row in table]
        if result == [0, 0, 0]:
            print(letters)
