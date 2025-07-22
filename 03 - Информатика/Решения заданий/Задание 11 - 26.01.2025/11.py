from math import ceil, log2

def cl(x): return ceil(log2(x))

n = 870
alloc = 150 * 1024
for k in range(1, 10000):
    N = 26 + 10 + 510
    i = cl(N)
    I = ceil(k * i / 8) * n
    if I > alloc:
        print(k)
        break
