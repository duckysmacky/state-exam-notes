def f(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '01'
    else:
        n2 += '10'
    return int(n2, 2)
for n in range(100000):
    R = f(n)
    if R > 101:
        print(R)
        break