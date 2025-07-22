def alg(n):
    n2 = bin(n)[2:]
    n2 += str(sum(map(int, n2)) % 2)
    n2 += str(sum(map(int, n2)) % 2)
    return int(n2, 2)

for n in range(10000):
    R = alg(n)
    if R > 630:
        print(n)
        break