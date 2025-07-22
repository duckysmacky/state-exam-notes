from math import ceil, log2

k = 128 * 128
N = 256
i = ceil(log2(N))
I = k * i
print(I / (1024 * 8))
