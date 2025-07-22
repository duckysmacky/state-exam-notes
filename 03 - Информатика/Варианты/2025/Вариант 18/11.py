from math import ceil, log2

k = 108
N = 10 + 60
i = ceil(log2(N))
I = ceil(k * i / 8)
n = 25_600
print(ceil(I * n / 1024))
