f = lambda A, x, y: ((x > 15) <= (x * y + 10 * x >= A)) and ((y * x + y > A) <= (y >= 1))
cnt = 0
for A in range(10000):
    for x in range(1000):
        for y in range(1000):
            if not f(A, x, y):
                break
        if not f(A, x, y):
            break
    else:
        cnt += 1
print(cnt)
