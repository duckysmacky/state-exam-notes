from math import ceil, log2

k = 1024 * 550
N = 567
i = ceil(log2(N))
I = k * i
packet = 480 * 1024 * 1024 * 8
print(packet / I)
