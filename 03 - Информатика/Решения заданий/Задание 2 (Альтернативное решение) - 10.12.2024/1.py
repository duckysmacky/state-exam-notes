from itertools import permutations, product

def f(x: int, y: int, z: int, w: int) -> bool:
    return ((z <= y) == (x <= (not w))) and (x or y)

for vals in product((0, 1), repeat=2):
    table = [
        (0, 1, 1, 1),
        (1, 0, 1, 0),
        (vals[0], 0, 0, vals[1])
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("xyzw", r=4):
        logic_table = [f(**dict(zip(letters, row))) for row in table]
        if logic_table == [0, 1, 1]:
            print(''.join(letters))