def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

val = 243 ** 540 - 6 * (9 ** 530) + 21 * (3 ** 511) - 3 * (3 ** 70) - 200
val9 = conv(val, 9)
print(val9.count('8'))
