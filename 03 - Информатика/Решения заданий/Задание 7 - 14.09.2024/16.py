k = 960 * 450
N = 3000 # 3000 -> 4096
i = 12
I_original = k * i
percent_compressed = 0.75
v = 2_563_120
t = 240
for n in range(1, 10_000):
    I_packet = n * I_original
    I_compressed_packet = I_packet * percent_compressed
    t = I_compressed_packet / v
    if t <= 240:
        print(t, n)