def D(n, m): return n % m == 0

for A in range(1, 1000):
    for x in range(1, 1000):
        f = (D(x, A) and not D(x, 12)) <= (not D(x, 18))
        if not f: break
    else:
        print(A)
        break
