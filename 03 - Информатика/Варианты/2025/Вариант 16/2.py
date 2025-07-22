from itertools import permutations, product

def f(w, x, z, y):
    return not (not y or not (not z or w)) and (z or (not w == x))

for n in product((0, 1), repeat=5):
    table = [
        (1, n[0], 1, 1),
        (n[1], n[2], 0, 0),
        (n[3], 0, 0, n[4])
    ]

    if len(set(table)) != 3: continue

    for letters in permutations("wxyz", r=4):
        result = [f(**dict(zip(letters, row))) for row in table]
        if result == [0, 1, 1]:
            print(''.join(letters))
