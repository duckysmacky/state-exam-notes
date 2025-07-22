for A in range(1, 1000):
    for x in range(1, 10_000):
        for y in range(1, 10_000):
            f = (3 * y - x < A) or (x >= 35) or (y >= 51)
            if not f: break
        if not f: break
    else:
        print(A)
        break
