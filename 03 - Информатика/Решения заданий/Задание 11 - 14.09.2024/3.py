from math import log2, ceil

k = 24
N = 24 + 10 # 34 -> 64
i = log2(64)
I = ceil(k * i / 8)
print(I * 100)
