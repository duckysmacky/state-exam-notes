def alg(s: str) -> str:
    while '355' in s or '25' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    return s

for n in range(0, 1000):
    s = '3' + '5' * n
    s = alg(s)
    if sum(map(int, s)) == 27:
        print(s, n)
