def conv(x: int, p: int) -> str:
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for x in range(2736):
    val = 5 ** 2025 + 5 ** 1500 - x
    val5 = conv(val, 5)
    if val5.count('0') == 527:
        print(x)
