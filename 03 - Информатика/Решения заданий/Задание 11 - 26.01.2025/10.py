from math import ceil, log2

def cl(x): return ceil(log2(x))

k = 21
N = 26 + 26 + 10
i = cl(N)
code = ceil(k * i / 8)

number = ceil(cl(1000) / 8)
extra = 55
I = code + number + extra
print(I)
