def f(s, e, p):
    if s > e: return 0
    if s == e: return p.count('*') == 2
    return f(s + 2, e, p + '+') + f(s + 3, e, p + '+') + f(s * 2, e, p + '*') + f(s * 3, e, p + '*')

print(f(1, 51, ''))
