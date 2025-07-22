from math import ceil, log2

k_code = 17
N_code = 26 + 26 + 10 + 6
i_code = ceil(log2(N_code))
I_code = ceil(k_code * i_code / 8)
N_num = 4001
i_num = ceil(log2(N_num))
I_num = ceil(i_num / 8)
I_extra = 70 - (I_code + I_num)
print(I_extra)