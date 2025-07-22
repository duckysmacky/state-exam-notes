x = 2
f = 54_000
t = 1.5 * 60
Imax = 30 * 1024 * 1024 * 8
for i in range(1, 100):
    I = f * x * t * i
    if I <= Imax:
        print(i)
