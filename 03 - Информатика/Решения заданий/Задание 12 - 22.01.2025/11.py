def alg(s: str) -> str:
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    return s

for n in range(3, 10_000):
    s = '5' + '2' * n
    s = alg(s)
    if sum(map(int, s)) == 64:
        print(s, n)
        break
