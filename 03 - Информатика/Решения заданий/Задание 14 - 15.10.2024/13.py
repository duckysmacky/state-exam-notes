def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for x in range(1, 2070 + 1):
    val = convert(7 ** 230 + 7 ** 130 + 7 ** 30 - x, 7)
    if val.count('0') == 199:
        print(x)