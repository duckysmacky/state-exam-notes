def alg(n):
    n2 = bin(n)[2:]
    if n % 5 == 0:
        n2 += n2[-2:]
    else:
        n2 += bin((n % 5) * 2)[2:]
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R < 150:
        print(n)