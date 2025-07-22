def alg(n):
    n2 = bin(n)[2:]
    n2 = n2[::-1]
    return int(n2, 2)

for n in range(1010, 10_000):
    R = alg(n)
    if R == 109:
        print(n)
        break