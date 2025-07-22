def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

print(convert(1024 ** 789 + 256 ** 678 - 64 ** 567, 5).count('4'))