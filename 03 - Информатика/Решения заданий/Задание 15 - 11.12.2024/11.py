def DEL(n, m): return n % m == 0

for A in range(1, 1000):
    for x in range(1, 10_000):
        f = (DEL(x, 2) <= (not DEL(x, 5))) or (x + A >= 70)
        if not f: break
    else:
        print(A)
        break
