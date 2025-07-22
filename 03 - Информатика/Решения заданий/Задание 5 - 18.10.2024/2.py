def alg(n):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', 'a').replace('1', 'b')
    n2 = n2.replace('a', '10').replace('b', '11')
    return int(n2, 2)

vals = []
for n in range(10000):
    R = alg(n)
    if R < 777 and R % 2 == 0:
        vals.append(R)
print(max(vals))