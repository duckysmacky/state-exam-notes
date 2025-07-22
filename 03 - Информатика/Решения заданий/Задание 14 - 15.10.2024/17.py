def convert(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

val = 49 * 52 ** 32 + 33 ** 123 + 74 * 43 ** 121 - 751235
ps = []
for p in range(2, 36):
    ps.append([convert(val, p).count('4'), p])
print(max(ps))