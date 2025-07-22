from itertools import product, permutations

def f1(x, y, z, w):
    return (w <= z) == (y <= x)

def f2(x, y, z, w):
    return (w <= z) and ((not x) == y)

for n in product((0, 1), repeat=3):
    table = [
        (0, n[0], 0, 0),
        (0, n[1], 1, 1),
        (0, 0, n[2], 0)
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        result = lambda f: [f(**dict(zip(letters, row))) for row in table]
        result1 = result(f1)
        result2 = result(f2)

        if result1 in ([0, 0, 0], [0, 1, 0]) and result2 in ([0, 0, 1], [1, 0, 1]):
            print(letters)
