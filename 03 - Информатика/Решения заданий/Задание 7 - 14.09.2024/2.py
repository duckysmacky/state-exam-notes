from math import log2

N = 1024
i = log2(N)
k = 320 * 260
I = k * i
I_min = I * 4
I_hour = I_min * 60
I_day = I_hour * 12
I_day -= I_min * 30
print(I_day / (1024 * 1024 * 8))