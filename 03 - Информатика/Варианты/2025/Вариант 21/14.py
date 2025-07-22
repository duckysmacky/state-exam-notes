import string

alph = string.digits + string.ascii_uppercase

# 1010 = 0 * 2 ** 0 + 1 * 2 ** 1 + 0 * 2 ** 2

def conv_from(num, base):
    num = num[::-1]
    vals = [alph.index(x) for x in num]
    return sum(vals[i] * (base ** i) for i in range(len(vals)))

for x in alph[:36]:
    val = int(f"12{x}{45}", 36) + conv_from(f"1{x}", 12345)
    if val % 13 == 0:
        print(x, val // 13)
