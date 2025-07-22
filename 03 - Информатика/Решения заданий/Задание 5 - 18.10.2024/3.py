def alg(n):
    n2 = bin(n - (n % 8))[2:]
    n2 += str(sum(map(int, n2)) % 2)
    n2 += str(sum(map(int, n2)) % 2)
    return int(n2, 2)

for n in range(100000):
    R = alg(n)
    if R < 86:
        print(bin(n)[2:])