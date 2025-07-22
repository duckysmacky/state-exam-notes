def replace(s, fr, to):
    return s.replace(fr, '*', 1).replace(fr, to, 1).replace('*', fr, 1)

def alg(s):
    while '666' in s or '999' in s:
        if '666' in s:
            s = replace(s, '666', '99')
        else:
            s = replace(s, '999', '66')
    return s

s = '9' * 130
print(alg(s))
