def alg(n):
    n2 = bin(n)[2:]
    if n % 11 == 0:
        n2 += '0' * n2.count('0')
    else:
        n2 = '1' * n2.count('1') + n2
    return int(n2, 2)

rs = []
for n in range(1, 100000):
    r = alg(n)
    if r % 317 == 0:
        rs.append(r)
print(min(rs))
