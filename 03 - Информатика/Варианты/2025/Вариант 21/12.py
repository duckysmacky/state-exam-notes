def alg(s: str) -> str:
    while '5555' in s:
        s = s.replace('5555', '33', 1)
        s = s.replace('333', '5', 1)
    return s

print(alg('5' * 150))