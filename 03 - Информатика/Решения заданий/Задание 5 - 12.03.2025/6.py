def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def alg(n):
    n4 = conv(n, 4)
    if n % 2 == 0:
        n4 += '02'
    else:
        n4 = '2' + n4 + '31'
    return int(n4, 4)

for n in range(1, 1000):
    r = alg(n)
    if r > 256:
        print(n)
        break
