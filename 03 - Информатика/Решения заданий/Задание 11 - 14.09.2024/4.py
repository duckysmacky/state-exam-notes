from math import log2, ceil

k = 450
N = 512
i = log2(N)
I = ceil(k * i / 8)
print(I * 16_384 / 1024)