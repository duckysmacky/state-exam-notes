def alg(s):
    while '5555' in s:
        s = s.replace('5555', '8', 1)
        s = s.replace('88', '5', 1)
    return s

cnt5 = []
for n in range(1000):
    s = '5' * (400 + n)
    res = alg(s)
    cnt5.append(res.count('5'))
n = cnt5.index(min(cnt5))
print(400 + n)
