def DEL(n, m):
    return n % m == 0


for A in range(1, 10_000):
    if not (not DEL(396, A) or not DEL(180, A)):
        print(A)
