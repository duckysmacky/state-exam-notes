from math import ceil, log2

n = 9999
I_total = 812 * 1024
N = 10 + 52 + 8139
i = ceil(log2(N))
for k in range(1, 10_000):
    I = ceil(k * i / 8)
    I_n = I * n
    if I_n <= I_total:
        print(k) # 47
print(ceil(47 * i / 8) * n / 1024)