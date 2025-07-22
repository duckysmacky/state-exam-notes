def Del(n, m): return n % m == 0

D = range(30, 46)
for A in range(1000):
    for x in range(1000):
        f = (not Del(x, 6) and x not in [45, 50, 55, 60]) <= (((abs(x - 15) <= 5) <= (x in D)) or (x & A != 0))
        if not f: break
    else:
        print(A)
        break
