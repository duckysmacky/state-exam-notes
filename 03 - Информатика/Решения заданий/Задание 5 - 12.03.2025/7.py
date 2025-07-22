def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def alg(n):
    n3 = conv(n, 3)
    if n % 3 == 0:
        n3 += n3[:2]
    else:
        n3 += conv((n % 3) * 7, 3)
    return int(n3, 3)

rs = []
for n in range(1, 1000):
    r = alg(n)
    if r > 260:
        rs.append(r)
print(min(rs))
