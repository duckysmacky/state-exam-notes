def alg(n):
    n2 = bin(n)[2:]
    n2 = n2[::-1]
    return int(n2, 2)

for n in range(1, 1001):
    if alg(n) == 23:
        print(n)
