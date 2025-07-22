from functools import lru_cache

@lru_cache
def f(n):
    if n == 1: return 1
    if n > 1: return 3 * f(n - 1) - g(n - 1)

@lru_cache
def g(n):
    if n == 1: return 1
    if n > 1: return 2 * f(n - 1) + 2 * g(n - 1) + n * n

print(sum(map(int, str(g(5)))))