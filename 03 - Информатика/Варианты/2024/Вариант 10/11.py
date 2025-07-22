from math import ceil, log2

cl = lambda x: ceil(log2(x))

k = 30
N = 5
i = cl(N)
I = ceil(k * i / 8)
print(I * 50)
