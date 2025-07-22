from itertools import product, permutations

def f(x, y, z, w):
    return x <= ((z <= y) <= w)

for n in product((0, 1), repeat=5):
    table = [
        (n[0], 1, 0, 0),
        (1, n[1], 0, n[2]),
        (0, n[3], n[4], 0)
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        result = [f(**dict(zip(letters, row))) for row in table]
        if result == [1, 0, 0]:
            print(letters)