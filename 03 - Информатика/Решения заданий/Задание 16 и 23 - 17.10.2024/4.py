def f(n):
    if n <= 4: return n
    if n > 4 and n % 2 == 0: return n + 4 * f(n - 1)
    if n > 4 and n % 2 != 0: return 2 * n * n * n + f(n - 1)
cnt = 0
for n in range(1, 400 + 1):
    if f(n) % 8 == 0: cnt += 1
print(cnt)