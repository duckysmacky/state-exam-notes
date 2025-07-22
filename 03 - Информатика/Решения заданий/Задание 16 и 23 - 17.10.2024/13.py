f = []
for _ in range(10): f.append([0] * 1_000_000)

for m in range(10):
    for n in range(500_000):
        if m == 0: f[m][n] = n + 1
        if m > 0 and n == 0: f[m][n] = f[m - 1][1]
        if m > 0 and n > 0: f[m][n] = f[m - 1][f[m][n - 1]]

print(f[4][1])