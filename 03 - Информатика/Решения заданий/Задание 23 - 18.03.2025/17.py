def conv(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

def f(s, e):
    if s < e: return 0
    if s == e: return 1
    return f(s - 2, e) + f(s // 3, e) + f(int(conv(s // 4, 8)), e)

print(f(98, 56) * f(56, 11))
