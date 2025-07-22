from math import ceil, log2

cl = lambda x: ceil(log2(x))

k = 256 * 2560
N = 256
i = cl(N)
v = 163_840 
t = 250
I = i * k
for n in range(10000):
    group = I * n
    time = group / v
    if time <= t:
        print(n)
