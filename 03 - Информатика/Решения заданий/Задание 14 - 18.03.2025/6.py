def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

val = 5 * 6 ** 1024 + 7 * 5 ** 1010 + 10 * 6 ** (5 * 106)
val9 = base(val, 9)
print(bin(val9.count('6')))
