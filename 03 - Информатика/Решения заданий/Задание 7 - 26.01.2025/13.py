f = 68_000
n = 22
t = 4 * 60 + 55
x = 2
header = 209 * 1024 * 8
v = 14_680_074
time = 500
for i in range(1, 100):
    I = f * i * t * x
    album = (I + header) * n
    if (album / v) <= time:
        print(i)
