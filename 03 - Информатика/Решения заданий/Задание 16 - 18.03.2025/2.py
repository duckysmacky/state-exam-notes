from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def f(n):
    if n >= 2025: return n
    return n // 2 + f(n + 3)

print(f(2020) - f(2023))
