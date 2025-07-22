def alg(n):
    n2 = bin(n)[2:]
    for _ in range(3):
        c0 = n2.count('0')
        c1 = n2.count('1')
        if c0 == c1:
            n2 += n2[-1]
        else:
            n2 += '1' if c1 < c0 else '0'
    return int(n2, 2)

for n in range(80):
    R = alg(n)
    if R % 2 == 0 and R % 4 != 0:
        print(n)
