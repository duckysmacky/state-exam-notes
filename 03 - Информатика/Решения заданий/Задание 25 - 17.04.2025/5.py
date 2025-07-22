def find_M(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            divs.append(x // div)
        if len(divs) == 3:
            break
    return divs[2] if len(divs) == 3 else 0

cnt = 0
N = 560_000_000
for num in range(N, N + 10_000):
    M = find_M(num)
    if M > 0:
        print(M)
        cnt += 1
    if cnt == 2:
        break