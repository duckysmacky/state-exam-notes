def find_sums(x: int) -> list:
    sq_sums = []
    for a in range(1, int(x ** 0.5) + 1):
        b = (x - a ** 2) ** 0.5
        if b == int(b) and a <= b:
            sq_sums.append((a, int(b)))
    return sq_sums

for num in range(225_600, 225_700 + 1):
    sq_sums = find_sums(num)
    if len(sq_sums) == 1:
        print(sq_sums[0][0], sq_sums[0][1])