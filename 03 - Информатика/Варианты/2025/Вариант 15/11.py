from math import ceil, log2

k = 6
N = 16 + 10
i = ceil(log2(N))
I = ceil(k * i / 8)
print(I * 40)
