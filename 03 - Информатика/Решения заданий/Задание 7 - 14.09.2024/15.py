from math import log2

k1 = 400 ** 2
N1 = 256
i1 = log2(N1)
I1 = 512 * 1024 * 1024 * 8
k2 = 100 ** 2
N2 = 16
i2 = log2(N2)
diff = (k1 * i1) / (k2 * i2)
I2 = I1 / diff / (1024 * 1024 * 8)
print(I2)