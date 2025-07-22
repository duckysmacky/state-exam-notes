from math import ceil, log2

k = 24
N = 15
i = ceil(log2(N))
I_log = ceil(k * i / 8)

k = 12
N = 10
i = ceil(log2(N))
I_pas = ceil(k * i / 8)

I = I_log + I_pas + 1
print(I * 40)
