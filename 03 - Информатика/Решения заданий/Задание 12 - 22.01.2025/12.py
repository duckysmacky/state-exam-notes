def alg(s: str) -> str:
    while '788' in s or '988' in s or '798' in s:
        if '788' in s:
            s = s.replace('788', '79', 1)
        if '988' in s:
            s = s.replace('988', '78', 1)
        if '798' in s:
            s = s.replace('798', '98', 1)
    return s

for n in range(2, 10_000):
    s = '7' + '8' * n
    s = alg(s)
    if sum(map(int, s)) == 17:
        print(n, n % 3 == 0)
