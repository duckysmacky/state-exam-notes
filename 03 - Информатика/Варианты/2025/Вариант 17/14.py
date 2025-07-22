def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for x in range(0, 1000):
    val = 4 * 625 ** 1920 + 4 * 125 ** x - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
    val5 = conv(val, 5)
    if val5.count('0') == 1891:
        print(x)
        break
