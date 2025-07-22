from math import ceil, log2

cl = lambda x: ceil(log2(x))

N = 10 + 900
i = cl(N)
I_n = 780 * 1024
alloc = I_n / 1500
for k in range(1, 100000):
    I = ceil(k * i / 8)
    if I <= alloc:
        print(k)
