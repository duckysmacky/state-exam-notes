from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def f(n):
    if n == 1: return 1
    if n > 1: return (2 * n - 2) * f(n - 1)

print(f(3029) // f(3027))
