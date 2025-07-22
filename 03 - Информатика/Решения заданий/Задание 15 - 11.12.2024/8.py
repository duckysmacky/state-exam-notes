for A in range(1000, 0, -1):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (15 * x - 2 * y + 37 != 0) or (A < x) or (A < y)
            if not f: break
        if not f: break
    else:
        print(A)
        break
