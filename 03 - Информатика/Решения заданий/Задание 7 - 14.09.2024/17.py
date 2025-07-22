k = 840 * 110
N = 2543 # -> 4096
i = 12
I_photo = k * i
percent_compressed = 0.5
v = 1_459_960
t_max = 237
for n in range(1, 10_000):
    I_packet = n * I_photo
    I_compressed_packet = I_packet * percent_compressed
    t = I_compressed_packet / v
    if t > t_max:
        n -= 1
        break
print(n, t)
for I_extra in range(1, 100_000_000):
    I_packet = n * I_photo + I_extra * 8
    I_compressed_packet = I_packet * percent_compressed
    t = I_compressed_packet / v
    if t > t_max:
        print(I_extra - 1)
        break