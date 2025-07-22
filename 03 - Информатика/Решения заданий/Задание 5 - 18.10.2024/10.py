def four(x: int) -> str:
    num = ""
    while x > 0:
        num += str(x % 4)
        x //= 4
    return num[::-1]

def alg(n):
    n4 = four(n)
    if n % 3 == 0:
        n4 += n4[-3:]
    else:
        n4 = four((n % 3) * 4) + n4
    return int(n4, 4)


print(alg(16), alg(99))
for n in range(1, 1000):
    R = alg(n)
    if R < 1166:
        print(n)