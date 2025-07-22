from math import ceil, log2

k = 512 * 512
N = 8192
i = ceil(log2(N))
print((k * i) / (1024 * 8))
