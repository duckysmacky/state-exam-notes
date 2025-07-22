from math import ceil, log2

for k in range(1000, 0, -1):
    N = 52 + 980
    i = ceil(log2(N))
    I = ceil(k * i / 8)
    I_n = I * 385 / 1024
    if I_n < 136:
        print(k)
        break