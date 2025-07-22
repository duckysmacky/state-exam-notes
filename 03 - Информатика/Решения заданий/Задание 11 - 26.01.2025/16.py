from math import ceil, log2

def cl(x): return ceil(log2(x))

k = 3000
N = 33 * 2 + 26 * 2 + 10 + 8
i = cl(N)
Imax = 1 * 1024
for x in range(0, 3000):
    K = k - x
    I = ceil(K * i / 8)
    if I <= Imax:
        print(x)
        break
