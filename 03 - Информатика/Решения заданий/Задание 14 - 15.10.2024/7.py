def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

print(bin(convert(64 ** 123 + 57 ** 371 - 23 ** 63, 16).count('B'))[2:])