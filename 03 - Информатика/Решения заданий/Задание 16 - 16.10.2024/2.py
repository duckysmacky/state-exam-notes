def F(n):
    if n == 1: return 2
    if n > 1: return 4 * F(n - 1) + 2 * n
print(F(8))