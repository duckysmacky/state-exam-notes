def DEL(n: int, m: int) -> bool: return n % m == 0

for A in range(1, 1000):
    for x in range(1, 10_000):
        f = (not DEL(x, 14) or not DEL(x, 4)) or (x + A >= 200)
        if not f: break
    else:
        print(A)
        break
