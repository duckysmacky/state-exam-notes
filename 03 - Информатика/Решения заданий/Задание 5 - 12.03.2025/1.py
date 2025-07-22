def alg(n):
    n2 = bin(n)[2:]
    if n % 2 != 0:
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '10'
    return int(n2, 2)

for n in range(1000):
    r = alg(n)
    if r > 697:
        print(n)
        break
