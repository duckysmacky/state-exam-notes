def f(n):
    if n < 4: return 4 * n - 1
    if n >= 4 and n % 2 == 0: return f(n - 2) + 2 * n
    if n >= 4 and n % 2 != 0: return f(n - 4) + 4 * n + 5
print(f(62))