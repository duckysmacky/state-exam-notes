def f(n):
    if n == 1: return 1
    if n > 1: return (3 * f(n - 1) - g(n - 1)) * 2


def g(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) - 3 * g(n - 1) + 1

print(f(7))