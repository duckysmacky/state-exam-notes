def alg(n):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        n2 = n2[:len(n2) // 2] + '1' + n2[len(n2) // 2:]
    return int(n2, 2)

for n in range(10000):
    R = alg(n)
    if R <= 68:
        print(n)