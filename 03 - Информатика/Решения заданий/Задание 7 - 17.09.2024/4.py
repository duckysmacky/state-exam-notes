k = 1024 * 512
n = 256
v = 6_393_911
t_max = 160
for i in range(1, 10_000):
    I_packet = k * i * n
    t = I_packet / v
    if t <= t_max:
        print(2 ** i)