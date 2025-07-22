k = 1920 * 1080
I_res = 1216 * 1024
I_alloc = 1215 * 1024 * 8

for i in range(1, 10_000):
    i_total = i + 1
    I = k * i_total
    I_compressed = I * 0.8
    if I_compressed <=I_alloc:
        print(2 ** i)