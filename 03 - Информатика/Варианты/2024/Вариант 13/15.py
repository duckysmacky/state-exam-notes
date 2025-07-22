def D(n: int, m: int) -> bool: return n % m == 0

for A in range(1, 1000):
    for x in range(1, 10000):
        f = D(x, A) <= ((not D(x, 35)) or D(x, 49))
        if not f: break
    else:
        print(A)
        break
