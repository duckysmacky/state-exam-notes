from functools import lru_cache

@lru_cache
def f(n):
    if n == 1: return 1
    if n > 1: return 3 * f(n - 1) + 2 * g(n - 1) + n * n

@lru_cache
def g(n):
    if n == 1: return 1
    if n > 1: return 2 * f(n - 1) + 3 * g(n - 1) + n * 5

num_sum = lambda x: sum(map(int, str(x)))
print(abs(num_sum(g(222)) - num_sum(f(333))))