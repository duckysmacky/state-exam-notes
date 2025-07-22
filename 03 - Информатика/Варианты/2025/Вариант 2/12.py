def alg(s: str) -> str:
    while '11111' in s or '222' in s:
        if '11111' in s:
            s = s.replace('11111', '22')
        else:
            s = s.replace('222', '2')
    return s

print(alg(2026 * '1'))
