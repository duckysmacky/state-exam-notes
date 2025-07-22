def triple(x: int) -> str:
    num = ""
    while x > 0:
        num += str(x % 3)
        x //= 3
    return num[::-1]

def alg(n):
    n3 = triple(n)
    if n % 3 == 0:
        n3 = n3[:2] + n3
    else:
        n3 += triple((n % 3) * 2)
    return int(n3, 3)

for n in range(1, 1000):
    R = alg(n)
    if R > 455:
        print(n)
        break