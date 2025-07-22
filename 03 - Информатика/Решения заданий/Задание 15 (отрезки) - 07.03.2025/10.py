def Del(n, m): return n % m == 0

B = range(45, 91)
cnt = 0
for A in range(1, 100):
    for x in range(1000):
        f = Del(x, 52) and not ((x not in B) or Del(x, A))
        if f: break
    else:
        cnt += 1
print(cnt)
