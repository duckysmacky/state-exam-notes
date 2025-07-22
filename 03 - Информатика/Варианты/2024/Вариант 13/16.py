def f(n: int) -> int:
    if n <= 1: return 1
    if n % 2 == 0 and n > 1: return 2 * n + f(n - 5)
    if n % 2 != 0 and n > 1: return 2 * f(n - 2)

print(f(20))
