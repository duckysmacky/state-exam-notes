def f(s, e):
    if s > e: return 0
    if s == e: return 1
    return f(s + 1, e) + f(int(f"1{s:b}", 2), e)

print(f(1, int('1111011', 2)))
