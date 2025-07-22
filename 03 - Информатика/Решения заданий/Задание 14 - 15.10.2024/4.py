def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

print(convert(1296 ** 625 * 216 ** 125 + 36 ** 25 - 6 ** 5, 6).count('5'))