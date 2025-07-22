from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

@lru_cache
def g(n):
    if n == 1: return 1
    if n > 1: return 11 * f(n - 1) + g(n - 1) * 2 - n * n

def f(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) + 3 * g(n - 1) + n

print(f(28) // g(14))
