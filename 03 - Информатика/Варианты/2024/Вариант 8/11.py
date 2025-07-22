from math import log2

# I = k * i
# N = 2 ** i

code_len = 13
code_symbols = 18 + 10 # 28
I_extra = 30
users = 60
# I_users = ? byte

k = code_len
N = 32 # 28 -> 32
i = log2(N) # 5
I_user = k * i // 8 + 1
I_user += I_extra
I_users = I_user * users
print(I_users)