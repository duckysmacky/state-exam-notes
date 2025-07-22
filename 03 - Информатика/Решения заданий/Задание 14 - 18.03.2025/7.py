def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

val = 25 ** 125 - 125 ** 10 * 25 ** 20 + 5 ** 5 - 5
val5 = base(val, 5)
print(val5.count('0'))
