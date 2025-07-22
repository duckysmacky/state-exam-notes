from itertools import product

def alg(s):
    while '00' not in s:
        s = s.replace('01', '130', 1)
        s = s.replace('02', '1013', 1)
        s = s.replace('03', '210', 1)
    return s

for n in range(1, 30):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = '0' + '1' * a + '2' * b + '3' * c + '0'
                res = alg(s)
                if res.count('1') == 28 and res.count('2') == 2:
                    print(len(s))
