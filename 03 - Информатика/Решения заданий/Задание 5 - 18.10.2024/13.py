def conv(x: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ""
    while x > 0:
        num += alph[x % 13]
        x //= 13
    return num[::-1]

def alg(n):
    n13 = conv(n)
    if int(n13[-1], 13) % 2 == 0:
        n13 = "1A" + n13[2:] + "B"
    else:
        n13 = "21" + n13[2:] + "A"
    return int(n13, 13)

vals = []
for n in range(1, 1000):
    R = alg(n)
    if R > 862: vals.append(R)
print(min(vals))