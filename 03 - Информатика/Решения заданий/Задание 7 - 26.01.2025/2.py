from math import ceil, log2

k = 1024 * 256
N = 2048
i = ceil(log2(N))
time = 24 * 60 * 60 / 15
I = k * i * time
print(I / (1024 * 1024 * 8))
