def D(n, m): return n % m == 0

for A in range(1, 1000):
    for x in range(1, 10000):
        f = (D(x, A) and D(x, 8)) <= ((not D(x, 8)) or D(x, 240))
        if not f: break
    else:
        print(A)
        break
