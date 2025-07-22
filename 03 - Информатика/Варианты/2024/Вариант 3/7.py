from math import ceil, log2

k = 320 * 600
I_alloc = 85 * 1024 * 8
for N in range(1, 10000):
    i = ceil(log2(N))
    I = k * i
    Ic = I * 0.8
    if Ic <= I_alloc:
        print(N)