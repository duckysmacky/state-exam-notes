from math import ceil, log2

k = 256
N = 10 + 1230
i = ceil(log2(N))
I = ceil(k * i / 8)
n = 19_648
In = I * n / 1024
print(In)