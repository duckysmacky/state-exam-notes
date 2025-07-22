def alg(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += n2[:2]
    else:
        n2 = f"1{n2}1"
    return int(n2, 2)

Rs = []
for n in range(10000):
    R = alg(n)
    if R > 700:
        Rs.append(R)
print(min(Rs))