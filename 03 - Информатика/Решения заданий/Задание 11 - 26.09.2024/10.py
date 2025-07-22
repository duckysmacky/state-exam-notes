from math import ceil, log2

k = 180
N = 10 + 6000
i = ceil(log2(N))
I = ceil((k * i) / 8)
n = 524_288
I_n = ceil((I * n) / 1024)
print(I_n)