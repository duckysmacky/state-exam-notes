import sys

sys.setrecursionlimit(10000)

def f(n):
    if n == 1: return 5
    if n > 1: return 2 * n + 1 + f(n - 1)

print(f(2024) - f(2022))
