for A in range(1, 1000):
    for x in range(1, 10_000):
        for y in range(1, 10_000):
            f = ((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)
            if not f: break
        if not f: break
    else:
        print(A)
        break
