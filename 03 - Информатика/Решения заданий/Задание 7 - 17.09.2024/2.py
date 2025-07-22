from math import ceil, log2

k = 1024 * 2048
N = 1024
i = ceil(log2(N))
I = k * i
v = 524_288
t_max = 320
for n in range(1, 10_000):
    I_packet = I * n
    t = I_packet / v
    if t <= t_max:
        print(n)