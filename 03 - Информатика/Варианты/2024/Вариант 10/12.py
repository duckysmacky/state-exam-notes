def alg(s: str) -> str:
    while '888' in s or '77' in s:
        if '888' in s:
            s = s.replace('888', '8777')
        else:
            s = s.replace('77', '8')
    return s

s = '8' * 100
res = alg(s)
print(res.count('7'))
