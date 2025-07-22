f = lambda A, x, y: (15 * x - y + 40 != 0) or (A < x) or (A < y)
for A in range(1000, 0, -1):
    if all(f(A, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
