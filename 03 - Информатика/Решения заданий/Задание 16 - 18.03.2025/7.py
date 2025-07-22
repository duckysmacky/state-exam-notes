from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def g(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) - g(n - 1) + 1

def f(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) - g(n - 1) - n

print(f(15) + g(15))
