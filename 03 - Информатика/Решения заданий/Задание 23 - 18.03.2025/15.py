def f(s, e, p):
    if s > 1000 or s <= 0: return 0
    if '****' in p or '--' in p: return 0
    if s == e: return 1
    return f(s - 1, e, p + '-') + f(s * 2, e, p + '*') + f(s * 3, e, p + '*')

print(f(4, 116, ''))
