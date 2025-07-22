def f(n):
    if n == 0: return 0
    if n > 0 and n % 3 == 0: return f(n - 1) + 3 * n
    if n > 0 and n % 3 > 0: return f(n - (n % 3)) + 8 * n - 2
print(f(30))