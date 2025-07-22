from math import ceil, log2

k = 1920 * 1920
N = 16_384
i = ceil(log2(N))
I = k * i
v = 1_474_560
t_max = 280
for n in range(1, 10_000):
    I_packet = I * n
    t = I_packet / v
    if t <= t_max:
        print(n)