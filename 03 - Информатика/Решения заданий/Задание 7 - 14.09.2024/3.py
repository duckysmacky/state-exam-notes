from math import log2

N = 256
i = log2(N)
k = 640 * 364
I_img = k * i
I_extra = 15 * 1024 * 8
I_logo = I_img + I_extra
n = (2 * 1024 * 1024 * 8) / I_logo
print(n)