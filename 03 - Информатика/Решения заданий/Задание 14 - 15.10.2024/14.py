def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for x in range(1, 2030 + 1):
    val = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    val = convert(val, 6)
    if val.count('0') == 202:
        print(x)