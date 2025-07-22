def alg(n):
    n2 = bin(n)[2:]
    n2 += n2[-1]
    if n2.count('1') % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    n2 += str(n2.count('1') % 2)
    return int(n2, 2)
for n in range(10_000):
    R = alg(n)
    if R > 130:
        print(n)
        break