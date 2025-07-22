k = 192 * 960
I_compressed = 75 * 1024 * 8
percent_compressed = 0.85
percent_original = 1
I_original = I_compressed / percent_compressed
i = I_original / k
print(i)