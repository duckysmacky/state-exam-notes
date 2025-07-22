def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def f(n):
    n4 = base(n, 4)
    if n % 4 == 0:
        n4 += n4[-2:]
    else:
        n4 += base((n % 4) * 2, 4)
    return int(n4, 4)

for n in range(1, 1000):
    r = f(n)
    if r < 261:
        print(n)
