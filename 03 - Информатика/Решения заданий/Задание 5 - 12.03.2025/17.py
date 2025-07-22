from string import digits, ascii_uppercase

def conv(x, p):
    alph = digits + ascii_uppercase
    num = ''
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

def alg(n):
    n17 = conv(n, 17)
    n17 = n17.replace('5', 'F')
    nsum = sum(int(x, 17) for x in n17)
    if nsum % 2 == 0:
        n17 += '11'
    else:
        n17 = '42' + n17
    return int(n17[::-1], 17)

for n in range(4, 1000):
    r = alg(n)
    if r % 7 == 0 and r > 290:
        print(n)
        break
