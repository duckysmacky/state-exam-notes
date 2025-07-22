def alg(n):
    n2 = bin(n)[2:]
    for _ in range(2):
        nsum = sum(map(int, n2))
        n2 += str(nsum % 2)
    return int(n2, 2)

rs = []
for n in range(1000):
    r = alg(n)
    if r > 680:
        rs.append(r)
print(min(rs))
