k = 1050 * 460
n = 64
v = 1_474_560
t = 200
for i in range(1, 100):
    I = k * i
    packet = I * n
    time = packet / v
    if time <= t:
        print(i, 2 ** i)
