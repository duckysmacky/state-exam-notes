for A in range(1, 1000):
    for x in range(10_000):
        f = (x & 45 != 0) <= ((x & 23 == 0) <= (x & A != 0))
        if not f: break
    else:
        print(A)
        break