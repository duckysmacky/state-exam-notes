def alg(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    return s

for n in range(101, 1000):
    s = '1' * n
    if alg(s) == '2':
        print(n)
        break
