def f(n):
    if n <= 14: return n * n * n + 22
    if n > 14 and n % 3 == 0: return f(n - 4) + f(n - 8)
    if n > 14 and n % 3 != 0: return f(n - 9) + n + 7
cnt = 0
for n in range(1, 199 + 1):
    if all(int(x) % 2 == 0 for x in str(f(n))):
        cnt += 1
print(cnt)