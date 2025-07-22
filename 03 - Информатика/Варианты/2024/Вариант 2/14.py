from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def conv(x: int, p: int) -> str:
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for x in alph[:11]:
    val = int(f"1800{x}6", 11) + int(f"6{x}107", 11) - int(f"1{x}63", 11)
    if val % 7 == 0:
        print(x, val // 7)