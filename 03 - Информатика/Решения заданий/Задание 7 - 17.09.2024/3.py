k = 1024 * 1024
n = 32
v = 1_474_560
t_max = 120
for i in range(1, 10_000):
    I_packet = k * i * n
    t = I_packet / v
    if t <= t_max:
        print(2 ** i)