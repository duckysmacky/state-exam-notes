DEL = lambda n, m: n % m == 0

for A in range(301, 100_000):
    valid = True
    for x in range(100_000):
        if not ((DEL(x, A) or (not DEL(x, 27) or not DEL(x, 89))) and (A > 300)):
            valid = False
            break
    if valid:
        print(A)
        break