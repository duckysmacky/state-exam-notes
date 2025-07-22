def convert(x: int) -> str:
    num = ""
    while x > 0:
        num += str(x % 3)
        x //= 3
    return num[::-1]

def alg(n):
    n3 = convert(n)
    if n % 3 == 0:
        n3 += n3[-3:]
    else:
        n3 += convert((n % 3) * 3)
    return int(n3, 3)

for n in range(1, 1000):
    R = alg(n)
    if R > 344:
        print(n)
        break