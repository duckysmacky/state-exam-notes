x = 4
f = 128_000
i = 16
I = 64 * 1024 * 1024 * 8
t = I / (x * f * i)

x = 2
f = 32_000
i = 4
I = x * f * i * t
print(I / (1024 * 1024 * 8))
