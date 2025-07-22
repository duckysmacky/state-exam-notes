def f(s, e):
    if s < e: return 0
    if s == 10: return 0
    if s == e: return 1
    return f(s - 1, e) + f(s // 2, e)

print(f(50, 20) * f(20, 1))
