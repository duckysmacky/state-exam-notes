def sum_divs(x: int) -> int:
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return div + (x // div)
    return 0

cnt = 0
for num in range(400_000, 400_000 + 1000):
    M = sum_divs(num)
    if str(M)[-1] == '8':
        print(num)
        cnt += 1
    if cnt == 5:
        break