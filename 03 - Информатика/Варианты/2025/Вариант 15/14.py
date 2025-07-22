def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for x in range(100000):
    val = 27 ** 7 - 3 ** 1 + 36 - x
    val3 = conv(val, 3)
    if sum(map(int, val3)) == 22:
        print(x)
        break
