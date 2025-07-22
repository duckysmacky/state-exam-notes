from math import ceil, log2

def cl(x): return ceil(log2(N))

k = 400
N = 10 + 4090
n = 16_384
i = ceil(log2(N))
I = k * i * n
print(I / (1024 * 8))
