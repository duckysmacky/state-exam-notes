from functools import lru_cache

@lru_cache()
def F(n):
    if n == 1: return 2
    if n % 2 == 0: return n + F(n / 2)
    if n > 1 and n % 2 != 0: return 5 * F(n - 1)


print(F(79))
