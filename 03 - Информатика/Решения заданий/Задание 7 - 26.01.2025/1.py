k = 1024 * 1280
Imax = 3 * 1024 * 1024 * 8
for i in range(1, 100):
    I = k * i
    if I <= Imax:
        print(i, 2 ** i)
