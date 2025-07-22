def find_M(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if div * div == x:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    divs.sort(reverse=True)
    return sum(divs[:2]) if len(divs) >= 2 else 0

N = 10_000_000
cnt = 0
for num in range(N, N + 100_000):
    M = find_M(num)
    if 0 < M < 10_000:
        print(M)
        cnt += 1
    if cnt == 5:
        break