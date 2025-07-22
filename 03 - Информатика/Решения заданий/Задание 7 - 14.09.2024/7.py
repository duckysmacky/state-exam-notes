k = 768 * 512
I = 640 * 1024 * 8
i_trans = 5
i = I / k
i = 13
i_color = i - i_trans
N = 2 ** i_color
print(N)