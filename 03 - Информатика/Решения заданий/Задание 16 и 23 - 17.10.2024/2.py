def f(n):
    if n == 1: return 2
    if n == 2: return 3
    if n > 2 and n % 2 != 0: return int((f(n - 2) + f(n - 2)) / 7)
    if n > 2 and n % 2 == 0: return 7 * n - int(f(n - 1) / 2 + 5)
print(f(40))