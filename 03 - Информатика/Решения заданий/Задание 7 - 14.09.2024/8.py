k = 64 * 1536
I = 252 * 1024 * 8
# 1 i_quality per 2 i_color
i = I / k # 21
i_color = 21 / 3 * 2
N = 2 ** i_color
print(N)