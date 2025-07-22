def find_M(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if div * div == x:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return (max(divs) - min(divs)) if len(divs) >= 2 else 0

cnt = 0
N = 350_000
for num in range(N, N + 10_000):
    M = find_M(num)
    if M % 23 == 9:
        print(num, M)
        cnt += 1
    if cnt == 6:
        break