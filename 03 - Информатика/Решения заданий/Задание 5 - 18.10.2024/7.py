def alg(n):
    n2 = bin(n)[2:]
    for _ in range(2):
        if sum(map(int, str(int(n2, 2)))) % 2 == 0:
            n2 += '0'
        else:
            n2 += '1'
    return int(n2, 2)

vals = []
for n in range(1000):
    R = alg(n)
    if R > 522: vals.append(R)
print(min(vals))