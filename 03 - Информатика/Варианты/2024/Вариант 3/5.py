def alg(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += "01"
    else:
        n2 = f"1{n2}10"
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R > 214:
        print(n)
        break