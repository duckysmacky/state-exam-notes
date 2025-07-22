from math import ceil, log2

N = 10 + 1234
i = ceil(log2(N))
I_n = 2050 * 1024
n = 65_536
Ia = I_n / n

for k in range(1, 10000):
    I = ceil(k * i / 8)
    if I <= Ia:
        print(k)