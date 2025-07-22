def R(x: int) -> int:
    num = bin(x)[2:]
    if x % 2 == 0:
        num += "00"
    else:
        num += "10"
    return int(num, 2)


for N in range(10_000):
    if R(N) > 130:
        print(N)
        break
