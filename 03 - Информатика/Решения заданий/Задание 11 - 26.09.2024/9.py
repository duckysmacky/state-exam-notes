from math import ceil, log2

k = 400
N = 10 + 4090
i = ceil(log2(N))
I = ceil((k * i) / 8)
n = 16_384
I_n = ceil((I * n) / 1024)
print(I_n)