def alg(s: str) -> str:
    while '06' in s or '566' in s or '666' in s:
        if '06' in s:
            s = s.replace('06', '6', 1)
        if '566' in s:
            s = s.replace('566', '60', 1)
        if '666' in s:
            s = s.replace('666', '5', 1)
    return s

def conv(x: int, p: int) -> str:
    from string import digits, ascii_uppercase
    alph = digits + ascii_uppercase
    num = ''
    while x > 0:
        num += alph[x % p]
        x //= p
    return num[::-1]

for n in range(3, 10_000):
    s = '0' + '6' * n
    s = alg(s)
    sum_s = sum(map(int, s))
    sum_s12 = conv(sum_s, 12)
    if '3' in sum_s12:
        print(n)
        break
