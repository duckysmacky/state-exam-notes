def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

print(convert(convert(5 ** 172 + 4 ** 347 - 8 ** 93, 4).count('0'), 8))