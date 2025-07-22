from math import ceil, log2

k = 158
N = 10 + 2022
i = ceil(log2(N))
I = ceil(k * i / 8)
print(ceil(I * 15_360 / 1024))
