def alg(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += bin(sum(map(int, n2)))[2:]
    else:
        n2 = f"1{n2}00"
    return int(n2, 2)

for n in range(1000):
    R = alg(n)
    if R > 843:
        print(n)
        break