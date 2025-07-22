from math import ceil, log2

k = 90
N = 10 + 1100
i = ceil(log2(N))
I = ceil(k * i / 8)
I_n = ceil(I * 17_408 / 1024)
print(I_n)