def alg(s: str) -> str:
    while '222' in s:
        s = s.replace('222', '3', 1)
        s = s.replace('333', '4', 1)
        s = s.replace('444', '2', 1)
    return s

s = '2' * 2022 + '4' * 2023
print(alg(s))
