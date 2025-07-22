def alg(n):
    n2 = bin(n)[2:]
    if sum(map(int, n2)) % 2 == 0:
        n2 = n2 + '10'
        n2 = '10' + n2[2:]
    else:
        n2 = n2 + '01'
        n2 = '11' + n2[2:]
    return int(n2, 2)

for n in range(1000):
    r = alg(n)
    if r <= 390:
        print(n)
