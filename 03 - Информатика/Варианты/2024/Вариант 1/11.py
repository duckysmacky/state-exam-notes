from math import ceil, log2

k = 10
N = 52
i = ceil(log2(N))
I = ceil(k * i / 8)
n = 65_536
I_n = I * n / 1024
print(I_n)