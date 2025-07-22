k = 1050 * 460
n_packet = 64
v = 1_474_560
t = 200
I_packet = v * t
I = I_packet / n_packet
i = I / k
i = 9
N = 2 ** i
print(N)