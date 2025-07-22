from math import ceil, log2

for N in range(1, 1000):
    k = 283
    i = ceil(log2(N))
    I = ceil(k * i / 8)
    I_n = I * 65_536 / 1024 / 1024
    if I_n > 15:
        print(N)
        break