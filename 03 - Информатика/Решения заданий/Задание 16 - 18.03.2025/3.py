from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1) * 2

print((f(2025) // 32 - f(2024)) / f(2023))
