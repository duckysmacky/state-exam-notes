from math import ceil, log2

for k in range(0, 1000):
    N = 10 + 52 + 5000
    i = ceil(log2(N))
    I = ceil(k * i / 8)
    I_n = I * 949 / 1024
    if I_n > 727:
        print(k)
        break