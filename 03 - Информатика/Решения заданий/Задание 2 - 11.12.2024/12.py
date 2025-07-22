from itertools import permutations

def f(x, y, z, w) -> bool:
    return ((((x and (not w)) <= ((w <= z) <= y) and (not (not y)) <= w) or (x and not (x <= z))) == (z == (not (z <= y))))

table = [
    (0, 1, 1, 0),
    (1, 0, 0, 1),
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 1, 1, 0),
    (0, 0, 0, 1)
]

for letters in permutations("xyzw", r=4):
    result = [f(**dict(zip(letters, row))) for row in table]
    if all(result):
        print(letters)
