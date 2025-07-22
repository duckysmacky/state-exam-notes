def alg(s: str) -> str:
    while '899' in s or '78' in s or '999' in s:
        if '899' in s:
            s = s.replace('899', '88', 1)
        if '78' in s:
            s = s.replace('78', '7', 1)
        if '999' in s:
            s = s.replace('999', '78', 1)
    return s

for n in range(3, 10_000):
    s = '7' + '8' * n
    s = alg(s)
    print(n, sum(map(int, s)))
