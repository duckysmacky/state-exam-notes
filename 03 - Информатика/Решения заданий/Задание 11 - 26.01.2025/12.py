from math import ceil, log2

def cl(x): return ceil(log2(x))

n = 7777
alloc = 566 * 1024
for k in range(1, 10000):
    N = 10 + 52 + 4044
    i = cl(N)
    I = ceil(k * i / 8) * n
    if I <= alloc:
        print(k)
