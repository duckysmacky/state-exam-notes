def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for x in range(19):
    val = int(f"55{convert(x, 19)}36", 19) + int(f"{convert(x, 19)}2524", 19)
    if val % 11 == 0:
        print(val // 11)
        break