def alg(n: int) -> int:
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2.replace('1', '11')
    else:
        n2 = n2.replace('0', '00')
    return int(n2, 2)

assert alg(4) == 12
assert alg(5) == 9

for n in range(1, 1000):
    R = alg(n)
    if R < 70 and R != n:
        print(n, R)
