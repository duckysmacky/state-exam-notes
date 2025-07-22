def alg(s):
    while '788' in s or '988' in s or '798' in s:
        if '788' in s:
            s = s.replace('788', '79', 1)
        if '988' in s:
            s = s.replace('988', '78', 1)
        if '798' in s:
            s = s.replace('798', '98', 1)
    return s

for n in range(10_000, 2, -1):
    s = '7' + '8' * n
    if sum(map(int, alg(s))) == 17:
        print(n)
