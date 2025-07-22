from functools import lru_cache


@lru_cache
def f(n):
    if n <= 1: return 1
    if n == 2: return 2
    if n > 2 and n % 3 == 0: return 2 * n - f(n // 3) - f(n - 1)
    if n > 2 and n % 3 != 0: return n + f(n - 2) + f(n // 10)

cnt = 0
for n in range(50, 100 + 1):
    if 50 < f(n) <= 200:
        cnt += 1
print(cnt)