from math import ceil, log2

n = 340
I_total = 160 * 1024
N = 10 + 26 + 1000
i = ceil(log2(N))
for k in range(1, 10_000):
    I_n = 0
    for _ in range(200):
        I_n += ceil((k + 3) * i / 8)
    for _ in range(140):
        I_n += ceil((k + 2) * i / 8)
    if I_n <= I_total:
        print(k)