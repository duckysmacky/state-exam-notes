def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

val = 59 ** 361 + 61 ** 539 - 39 ** 651 - 361
val2 = bin(val)[3:]
sum2 = sum(map(int, val2))
print(base(sum2, 8))
