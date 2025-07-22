def alg(n):
    n2 = bin(n)[2:]
    n2 += n2[-1]
    n2 += '0' if n2.count('1') % 2 == 0 else '1'
    n2 += '0' if n2.count('1') % 2 == 0 else '1'
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R > 90:
        print(n)
        break
