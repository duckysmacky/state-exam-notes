for A in range(1000):
    for x in range(1000):
        for y in range(1000):
            f = (4 * x + y < A) or (x < y) or (22 <= x)
            if not f: break
        if not f: break
    else:
        print(A)
        break
