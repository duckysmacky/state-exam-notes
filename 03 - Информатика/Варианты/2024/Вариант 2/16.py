f = [0] * 1605
for n in range(1605):
    if n == 1: f[n] = 1
    if n == 2: f[n] = 4
    if n > 2: f[n] = f[n - 1] + (n - 1) * f[n - 2]

print(f[1604] / f[1600])