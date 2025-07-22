def DEL(n, m): return n % m == 0

for A in range(1000, 0, -1):
    for x in range(1, 10_000):
        f = ((DEL(x, 24) and DEL(x, 36)) <= DEL(x, A)) and (A ** 2 - A - 5000 < 112)
        if not f: break
    else:
        print(A)
        break
