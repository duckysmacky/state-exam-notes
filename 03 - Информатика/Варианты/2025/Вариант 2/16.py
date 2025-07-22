f = [0] * 3001
for n in range(3001):
    if n == 1: f[n] = 1
    if n > 1: f[n] = n * f[n - 1]

print(((f[3000] // 150) + f[2999]) / f[2998])
