def R(N: int) -> int:
    summ = sum([int(x) for x in str(N)])
    num = bin(summ)[2:]
    if num.count('1') % 2 == 0:
        num = f"1{num}00"
    else:
        num = f"10{num}1"
    return int(num, 2)


count = 0
for N in range(100_000_000, 999_999_999 + 1):
    if R(N) == 21:
        count += 1
        print(N, R(N))
print(count)