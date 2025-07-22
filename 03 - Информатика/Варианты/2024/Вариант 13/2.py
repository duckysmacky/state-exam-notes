from itertools import product, permutations

def f(x, y, z, w) -> bool:
    return not (x and y) and (z or not x) or w

for n in product((0, 1), repeat=6):
    table = [
        (n[0], n[1], 1, n[2]),
        (1, 0, 0, n[3]),
        (0, n[4], n[5], 1)
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        logic_table = [f(**dict(zip(letters, row))) for row in table]
        if logic_table == [0, 0, 0]:
            print(''.join(letters))
