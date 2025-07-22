from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def f(n):
    if n == 0: return 1
    if n == 1: return 2
    if n % 2 == 0 and n > 1: return 7 + int(3 * f(n - 2) / 2)
    if n % 2 != 0 and n > 1: return 6 * n + int((f(n - 2) + f(n - 1) + 8) / 5)

print(f(71))
