for A in range(1, 100_000):
    for x in range(1, 100_000):
        if not ((not ((x & A) != 0)) or ((not ((x & 14) == 0)) or ((x & 17) != 0))):
            break
    else:
        print(A)