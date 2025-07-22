def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

val = 654 ** 25 + 927 ** 13 + 243 ** 5 - 44 ** 2 + 2025
print(sum(n.isalpha() for n in convert(val, 25)))