cnt = 0
for A in range(0, 1000):
    for x in range(1, 100 + 1):
        for y in range(1, 100 + 1):
            f = ((y > A) or (x * y < 2 * A) <= (A * y < 30)) or ((2 * y + 4 * x) < A)
            if not f: break
        if not f: break
    else:
        print(A)
        cnt += 1
        if cnt == 8: break
