def angle(*angles) -> bool:
    return sum(angles) == 180

for A in range(1, 1000):
    for x in range(1, 1000):
        f = angle(47, A, x + 40) == (angle(A, x, 45) and (not (A + 30 < 156)))
        if not f: break
    else:
        print(A)
        break
