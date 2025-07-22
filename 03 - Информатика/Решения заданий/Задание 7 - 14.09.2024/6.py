from math import log2

k = 128 * 512
N = 2048
i = log2(N)
I_compressed = 44 * 1024 * 8
I_original = k * i
percent = I_compressed / I_original
print(percent)