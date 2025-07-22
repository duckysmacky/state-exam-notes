from functools import lru_cache
import sys

sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(100000)

def g(n):
    if n == 1: return 1
    if n > 1: return n * g(n - 1)

def f(n):
    if n <= 7342: return g(n)
    if n > 7342 and n % 2 == 0: return f((n // 3) - 278) + n
    if n > 7342 and n % 2 != 0: return f(n - 1) + g(n // 57) + 5

r = f(982134) + g(241)
print(sum(map(int, str(r))))
