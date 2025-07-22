for A in range(1, 1000):
    for x in range(1, 10_000):
        f = (x & A != 0) <= ((x & 31 == 0) <= (x & 61 != 0))
        if not f: break
    else:
        print(A)
        break
