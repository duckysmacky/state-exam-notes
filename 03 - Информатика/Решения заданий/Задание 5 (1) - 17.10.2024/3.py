def alg(n):
    n2 = bin(n)[2:]
    n2 += n2[-1]
    n2 += str(bin(n)[2:].count('1') % 2)
    n2 += str(n2.count('1') % 2)
    return int(n2, 2)

Rs = []
for n in range(100000):
    R = alg(n)
    if R > 40:
        Rs.append(R)
print(min(Rs))