def alg(n):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', 'a').replace('1', 'b')
    n2 = n2.replace('a', '1').replace('b', '0')
    return int(n2, 2)

for n in range(10000):
    R = n - alg(n)
    if R == 817:
        print(n)
        break