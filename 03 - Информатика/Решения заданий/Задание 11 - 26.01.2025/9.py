from math import ceil, log2

def cl(x): return ceil(log2(x))

k = 15
N = 26 + 4
i = cl(N)
code = ceil(k * i / 8)
number = ceil(cl(10000) / 8)
n = 1000
I = (code + number) * n
print(I)
