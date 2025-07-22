import sys

sys.setrecursionlimit(10 ** 9)

def F(n: int) -> int:
    if n == 1: return 1
    if n > 1: return n + F(n - 1)

count = 0
res = F(2023)
for n in range(1, 100 + 1):
    if (res // F(n)) % 2 == 0:
        count +=1
print(count)