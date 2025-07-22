def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for x in range(1, 5871):
    val = 4 ** 420 + 4 ** 310 + 4 ** 20 - x
    val4 = base(val, 4)
    if val4.count('2') == 7:
        print(x)
