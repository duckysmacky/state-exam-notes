from math import ceil, log2

k_code = 21
N_code = 26 + 26 + 10
i_code = ceil(log2(N_code))
I_code = ceil(k_code * i_code / 8)
N_num = 1001
i_num = ceil(log2(N_num))
I_num = ceil(i_num / 8)
I_extra = 55
I_total = I_code + I_num + I_extra
print(I_total)