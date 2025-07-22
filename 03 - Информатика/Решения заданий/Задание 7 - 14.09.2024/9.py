from math import log2

n_packet = 1024
k = 1024 * 512
N = 256
i = log2(N)
I = k * i / (1024 * 8)
I_packet = n_packet * I
print(I_packet)