alloc = 125 * 1024 * 1024 * 8
x = 2
f = 15_000
i = 16
I = alloc / 0.25
t = I / (x * f * i)
print(t / 60)
