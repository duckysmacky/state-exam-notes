def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for x in range(1, 6030):
    val = 9 ** 260 + 9 ** 160 + 9 ** 60 - x
    val9 = base(val, 9)
    if val9.count('5') > val9.count('6') and val9.count('6') > 0:
        print(x)
        break
