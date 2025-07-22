def alg(n):
    n2 = bin(n)[2:]
    if sum(map(int, n2)) % 2 == 0:
        n2 = "10" + n2[2:] + "0"
    else:
        n2 = "11" + n2[2:] + "11"
    return int(n2, 2)

Ns = []
for N in range(100000):
    R = alg(N)
    if R < 99:
        Ns.append(N)
print(max(Ns))