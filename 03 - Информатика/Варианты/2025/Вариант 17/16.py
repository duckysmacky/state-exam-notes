f = [0] * 4965
for n in range(4965):
    if n <= 3: f[n] = n - 1
    if n > 3 and n % 2 == 0: f[n] = f[n - 2] + n / 2 - f[n - 4]
    if n > 3 and n % 2 != 0: f[n] = f[n - 1] * n + f[n - 2]

print(f[4952] + 2 * f[4958] + f[4964])
