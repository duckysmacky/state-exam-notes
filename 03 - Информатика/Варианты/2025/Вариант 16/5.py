def alg(n):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        i = len(n2) // 2
        n2 = n2[:i] + '1' + n2[i:]
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R >= 26:
        print(n)
        break
