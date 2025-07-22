from math import ceil, log2

n = 940
I_total = 170 # kb
N = 10 + 26 + 1000
i = ceil(log2(N))
for k in range(1, 10_000):
    I = ceil(k * i / 8)
    I_n = I * n / 1024
    if I_n <= I_total:
        print(k)