from math import ceil, log2

k = 512 * 320
I_res = 60 * 1024 * 8
for N in range(1, 1025):
    i = ceil(log2(N))
    I = i * k
    if I <= I_res:
        print(N)
