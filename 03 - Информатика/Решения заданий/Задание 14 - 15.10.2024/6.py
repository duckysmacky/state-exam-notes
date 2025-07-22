def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

print(convert(convert(35 ** 28 + 92 ** 15 - 12 ** 5, 5).count('3'), 9))