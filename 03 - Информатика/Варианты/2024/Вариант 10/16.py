from functools import lru_cache

@lru_cache
def f(n):
    if n > 30: return n * n + 3 * n + 5
    if n % 2 == 0 and n <= 30: return 2 * f(n + 1) + f(n + 4)
    if n % 2 != 0 and n <= 30: return f(n + 2) + 3 * f(n + 5)

cnt = 0
for n in range(1, 1001):
    res = str(f(n))
    if res.count('0') >= 2:
        cnt += 1
print(cnt)
