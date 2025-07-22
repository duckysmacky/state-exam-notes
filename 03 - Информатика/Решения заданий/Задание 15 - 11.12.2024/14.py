def tri(*sides):
    sides = sorted(list(sides))
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

cnt = 0
for A in range(10, 99 + 1, 2):
    for x in range(1, 100):
        for y in range(1, 100):
            f = tri(16, y, A) or tri(x, y, A) == (x + A < 85)
            if not f: break
        if not f: break
    else:
        cnt += 1
print(cnt)
