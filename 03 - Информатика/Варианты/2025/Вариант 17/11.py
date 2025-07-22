from math import ceil, log2

k = 23
I_n = 21 * 1024 * 1024
n = 500_000
alloc = I_n / n
for N in range(1, 10000000):
    i = ceil(log2(N))
    I = ceil(i * k / 8)
    if I <= alloc:
        print(N)
