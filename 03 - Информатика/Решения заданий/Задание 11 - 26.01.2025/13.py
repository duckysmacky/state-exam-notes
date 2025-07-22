from math import ceil, log2

def cl(x): return ceil(log2(x))

alloc = 8 * 1024 * 1024
n = 32768
for N in range(1, 10000):
    k = 256
    i = cl(N)
    I = ceil(k * i / 8) * n
    if I > alloc:
        print(N)
        break
