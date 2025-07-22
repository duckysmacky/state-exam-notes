from math import ceil, log2

k = 1024 * 1024
alloc = 600 * 1024 * 8
I = alloc * 1.15
i = I // k
print(2 ** i)
