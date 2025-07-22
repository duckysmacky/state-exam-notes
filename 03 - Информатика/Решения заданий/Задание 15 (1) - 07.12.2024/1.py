def DEL(n: int, m: int) -> bool: return n % m == 0

for A in range(1, 1000):
    for x in range(10_000):
        f = DEL(x, 15) <= (DEL(x, A) or not DEL(x, 3))
        if not f: break
    else:
        print(A)