def alg(s):
    while '>9' in s or '>1' in s or '>3' in s:
        if '>9' in s:
            s = s.replace('>9', '13>1', 1)
        if '>1' in s:
            s = s.replace('>1', '13>', 1)
        if '>3' in s:
            s = s.replace('>3', '99>1', 1)
    return s

s = '>' + '9' * 30 + '1' * 17 + '3' * 19
res = alg(s)
print(sum(map(int, res.replace('>', ''))))
