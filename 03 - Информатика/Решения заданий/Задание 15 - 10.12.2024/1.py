f = lambda A, x, y: ((y + 10 * x != 28) or (A > x - 1)) and (A < y + 50)
for A in range(1, 10_000):
    if all(f(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
