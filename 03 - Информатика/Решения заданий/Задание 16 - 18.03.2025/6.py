from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

def f(n):
    if n <= 19: return n * n * n + 22
    if n % 3 == 0 and n > 19: return f(n - 4) + f(n - 8)
    if n % 3 != 0 and n > 19: return f(n - 9) + n + 7

cnt = 0
for n in range(1, 101):
    r = f(n)
    if all([x % 2 == 0 for x in list(map(int, str(r)))]): cnt += 1
print(cnt)
